frappe.ui.form.on('Timesheet', {
	refresh: function(frm) {
		// Hide the Connections section
		$('.form-links').hide();
	}
});

frappe.ui.form.on('Timesheet',{
	onload (frm) {
	setTimeout(() => {
		// $("[data-doctype='Timesheet']").hide()
		$("[data-doctype='Sales Invoice']").hide()
		}, 10);
	}
})