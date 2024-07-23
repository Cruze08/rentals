import frappe

@frappe.whitelist(allow_guest = True)

def get_char():
    return "A"