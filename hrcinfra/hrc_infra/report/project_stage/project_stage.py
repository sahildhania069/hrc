# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


import frappe
from frappe import _


def execute(filters=None):
	columns = get_columns()
	data = []

	data = frappe.db.get_all(
		"Stage",
		# filters=filters,
		# fields=[
		# 	"name",
		# ],
		# order_by="expected_end_date",
	)
	print(data)
	print(len(data))


	# for stage in data:
	# 	stage["
		
	
	print("Data",data)

	chart = get_chart_data(data)
	report_summary = get_report_summary(data)

	return columns, data, None, chart, report_summary


def get_columns():
	return [
		# {
		# 	"fieldname": "name",
		# 	"label": _("Stage"),
		# 	"fieldtype": "Link",
		# 	"options": "Project",
		# 	"width": 200,
		# },
		# {
		# 	"fieldname": "project_type",
		# 	"label": _("Type"),
		# 	"fieldtype": "Link",
		# 	"options": "Project Type",
		# 	"width": 120,
		# },
		# # {
		# 	"fieldname": "project_type",
		# 	"label": _("Type"),
		# 	"fieldtype": "Link",
		# 	"options": "Project Type",
		# 	"width": 120,
		# },
	# 	{"fieldname": "custom_stage", "label": _("custom_stage"), "fieldtype": "Data", "width": 120},
	# 	{"fieldname": "total_project", "label": _("Total Tasks"), "fieldtype": "Data", "width": 120},
	# 	{
	# 		"fieldname": "foundation",
	# 		"label": _("Tasks foundation"),
	# 		"fieldtype": "Data",
	# 		"width": 120,
	# 	},
	# 	{"fieldname": "erection", "label": _("Tasks erection"), "fieldtype": "Data", "width": 120},
	# 	{"fieldname": "percent_complete", "label": _("Completion"), "fieldtype": "Data", "width": 120},
	# 	{
	# 		"fieldname": "expected_start_date",
	# 		"label": _("Start Date"),
	# 		"fieldtype": "Date",
	# 		"width": 120,
	# 	},
	# 	{"fieldname": "expected_end_date", "label": _("End Date"), "fieldtype": "Date", "width": 120},
	]


def get_chart_data(data):
	labels = []
	total = []
	foundation = []
	erection = []
	stringing = []
	procurement = []
	

	for stage in data:
		pass
		# labels.append(stage.name)
		# total.append(stage.total_project)
		# erection.append(stage.erection)

	foundation_n = frappe.db.count(
		"Project", filters={"custom_stage": "Foundation"}
		)
	erection_n = frappe.db.count(
			"Project", filters={"custom_stage": "Erection"}
		)
	stringing_n = frappe.db.count(
			"Project", filters={"custom_stage": "Stringing"}
		)
	procurement_n = frappe.db.count(
			"Project", filters={"custom_stage": "Procurement"}
		)

	foundation.append(foundation_n)
	erection.append(erection_n)
	stringing.append(stringing_n)
	procurement.append(procurement_n)
	labels.append("Project Stage")

	return {
		"data": {
			"labels": labels[:30],
			"datasets": [
				{"name": _("Foundation"), "values": foundation[:30]},
				{"name": _("Erection"), "values": erection[:30]},
				{"name": _("Stringing"), "values": stringing[:30]},
				{"name": _("Procurement"), "values": procurement[:30]},

			],
		},
		"type": "bar",
		"colors": ["#fc4f51", "#78d6ff", "#7575ff"],
		# "barOptions": {"stacked": True},
	}


def get_report_summary(data):
	if not data:
		return None

	# avg_completion = sum(stage.percent_complete for stage in data) / len(data)
	total = frappe.db.count("Project")
	foundation = frappe.db.count(
		"Project", filters={"custom_stage": "Foundation"}
		)
	erection = frappe.db.count(
			"Project", filters={"custom_stage": "Erection"}
		)
	stringing = frappe.db.count(
			"Project", filters={"custom_stage": "Stringing"}
		)
	procurement = frappe.db.count(
			"Project", filters={"custom_stage": "Procurement"}
		)

	# erection = data.stage.ere
	# foundation = data[""]
	
	# for stage in data:
	# 	print(stage)
	# 	name = f"{stage.name}"
	# 	name = stage[f"{stage.name}"]

	return [
		# {
		# 	"value": avg_completion,
		# 	"indicator": "Green" if avg_completion > 50 else "Red",
		# 	"label": _("Average Completion"),
		# 	"datatype": "Percent",
		# },
		{
			"value": total,
			"indicator": "Blue",
			"label": _("Total Project"),
			"datatype": "Int",
		},
		{
			"value": foundation,
			"indicator": "Green",
			"label": _("Under Founation"),
			"datatype": "Int",
		},
		{
			"value": erection,
			"indicator": "Green",
			"label": _("Under Erection"),
			"datatype": "Int",
		},
		{
			"value": stringing,
			"indicator": "Green",
			"label": _("Under Stringing"),
			"datatype": "Int",
		},
		{
			"value": procurement,
			"indicator": "Green",
			"label": _("Under Procurement"),
			"datatype": "Int",
		},
		# {
		# 	"value": erection,
		# 	"indicator": "Green" if erection == 0 else "Red",
		# 	"label": _("erection Tasks"),
		# 	"datatype": "Int",
		# },
	]
