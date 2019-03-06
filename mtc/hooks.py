# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "mtc"
app_title = "Mtc"
app_publisher = "riyas"
app_description = "mtc "
app_icon = "octicon  	"
app_color = "grey"
app_email = "riyaspangode@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/mtc/css/mtc.css"
# app_include_js = "/assets/mtc/js/mtc.js"

# include js, css files in header of web template
# web_include_css = "/assets/mtc/css/mtc.css"
# web_include_js = "/assets/mtc/js/mtc.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"MTC Requests" : "public/js/mtc_requests.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "mtc.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "mtc.install.before_install"
# after_install = "mtc.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "mtc.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"mtc.tasks.all"
# 	],
# 	"daily": [
# 		"mtc.tasks.daily"
# 	],
# 	"hourly": [
# 		"mtc.tasks.hourly"
# 	],
# 	"weekly": [
# 		"mtc.tasks.weekly"
# 	]
# 	"monthly": [
# 		"mtc.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "mtc.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "mtc.event.get_events"
# }

