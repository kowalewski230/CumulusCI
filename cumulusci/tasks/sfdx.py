""" Wrapper tasks for the SFDX CLI


TODO: Instead of everyone overriding random attrs, especially as future
users subclass these tasks, we should expose an api for the string format
function. i.e. make it easy for subclasses to add to the string inherited
from the base.

Actually do this in Command. have it expose command segments.

Then here in SFDX we will add an additional metalayer for
how the CLI formats args opts commands etc.
"""
import json

from cumulusci.core.config import ScratchOrgConfig
from cumulusci.core.tasks import BaseTask
from cumulusci.tasks.command import Command

SFDX_CLI = "sfdx"


class SFDXBaseTask(Command):
    """ Call the sfdx cli with params and no org """

    task_options = {
        "command": {
            "description": "The full command to run with the sfdx cli.",
            "required": True,
        },
        "extra": {"description": "Append additional options to the command"},
    }

    def _init_options(self, kwargs):
        super(SFDXBaseTask, self)._init_options(kwargs)
        self.options["command"] = self._get_command()
        # Add extra command args from
        if self.options.get("extra"):
            self.options["command"] += " {}".format(self.options["extra"])

    def _get_command(self):
        command = "{SFDX_CLI} {command}".format(
            command=self.options["command"], SFDX_CLI=SFDX_CLI
        )
        return command


class SFDXOrgTask(SFDXBaseTask):
    """ Call the sfdx cli with a workspace username """

    salesforce_task = True

    def _init_options(self, kwargs):
        super(SFDXOrgTask, self)._init_options(kwargs)

        # Add username to command if needed
        self.options["command"] = self._add_username(self.options["command"])

        self.logger.info("Running command:  {}".format(self.options["command"]))

    def _add_username(self, command):
        # For scratch orgs, just pass the username in the command line
        if isinstance(self.org_config, ScratchOrgConfig):
            command += " -u {username}".format(username=self.org_config.username)
        return command

    def _get_env(self):
        env = super(SFDXOrgTask, self)._get_env()
        if not isinstance(self.org_config, ScratchOrgConfig):
            # For non-scratch keychain orgs, pass the access token via env var
            env["SFDX_INSTANCE_URL"] = self.org_config.instance_url
            env["SFDX_USERNAME"] = self.org_config.access_token
        return env


class SFDXJsonTask(SFDXOrgTask):
    command = "force:mdapi:deploy --json"

    def _process_output(self, line):
        try:
            data = json.loads(line)
        except Exception:
            self.logger.error("Failed to parse json from line: {}".format(line))
            return

        self._process_data(data)

    def _init_options(self, kwargs):
        kwargs["command"] = self._get_command()
        super(SFDXJsonTask, self)._init_options(kwargs)

    def _get_command(self):
        command = "{SFDX_CLI} {command}".format(command=self.command, SFDX_CLI=SFDX_CLI)
        command = self._add_username(command)
        return command

    def _process_data(self, data):
        self.logger.info("JSON = {}".format(data))


class ChooseDeploymentMethod(BaseTask):
    """Choose whether to deploy using SFDX or the metadata API.
    """

    def _run_task(self):
        is_dx_format = self.project_config.project__source_format == "sfdx"
        is_scratch_org = self.org_config.scratch
        self.return_values = {
            "dx": is_dx_format and is_scratch_org,
            "md": not is_dx_format or not is_scratch_org,
            "convert": is_dx_format and not is_scratch_org,
        }
