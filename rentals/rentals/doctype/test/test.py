# Copyright (c) 2024, Ankit and contributors
# For license information, please see license.txt

# import frappe

#import frappe
# your_app/your_module/doctype/your_doctype/your_doctype.py

import frappe
from frappe.model.document import Document

class test(Document):
    def after_save(self):
        self.naming_series = self.city[0].upper()