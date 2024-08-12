# Copyright (c) 2024, TCB InfoTech and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document



class DPR(Document):
	def on_submit(self):
		project=self.project
		doc=frappe.get_doc("Project",project)
		doc.custom_stage=self.stage
		doc.save()