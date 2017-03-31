#!/usr/bin/env python
"""This module loads all the selenium tests for the GUI."""



# pylint: disable=unused-import
from grr.gui.plugins import acl_manager_test
from grr.gui.plugins import api_docs_test
from grr.gui.plugins import artifact_manager_test
from grr.gui.plugins import artifact_view_test
# This wasn't run for a long time and exposes bugs that need to be fixed before
# it can be enabled
# from grr.gui.plugins import crash_view_test
from grr.gui.plugins import cron_view_test
from grr.gui.plugins import dir_refresh_test
from grr.gui.plugins import fileview_test
from grr.gui.plugins import flow_archive_test
from grr.gui.plugins import flow_copy_test
from grr.gui.plugins import flow_create_hunt_test
from grr.gui.plugins import flow_export_test
from grr.gui.plugins import flow_management_test
from grr.gui.plugins import flow_notifications_test
from grr.gui.plugins import forms_test
from grr.gui.plugins import hosttable_test
from grr.gui.plugins import hunt_archive_test
from grr.gui.plugins import hunt_control_test
from grr.gui.plugins import hunt_view_test
from grr.gui.plugins import inspect_view_test
from grr.gui.plugins import main_content_view_test
from grr.gui.plugins import navigator_view_test
from grr.gui.plugins import new_hunt_test
from grr.gui.plugins import notifications_test
from grr.gui.plugins import rekall_viewer_test
from grr.gui.plugins import report_test
from grr.gui.plugins import searchclient_test
from grr.gui.plugins import server_load_view_test
from grr.gui.plugins import settings_view_test
from grr.gui.plugins import timeline_test
from grr.gui.plugins import userdashboard_test
from grr.gui.plugins import vfsview_test
