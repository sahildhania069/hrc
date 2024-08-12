// // Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// // For license information, please see license.txt

// frappe.query_reports["Project Stage"] = {
// 	filters: [
// 		{
// 			fieldname: "company",
// 			label: __("Company"),
// 			fieldtype: "Link",
// 			options: "Company",
// 			default: frappe.defaults.get_user_default("Company"),
// 			reqd: 1,
// 		},
// 		{
// 			fieldname: "is_active",
// 			label: __("Is Active"),
// 			fieldtype: "Select",
// 			options: "\nYes\nNo",
// 			default: "Yes",
// 		},
// 		{
// 			fieldname: "status",
// 			label: __("Status"),
// 			fieldtype: "Select",
// 			options: "\nOpen\nCompleted\nCancelled",
// 			default: "Open",
// 		},
// 		{
// 			fieldname: "project_type",
// 			label: __("Project Type"),
// 			fieldtype: "Link",
// 			options: "Project Type",
// 		},
// 		{
// 			fieldname: "priority",
// 			label: __("Priority"),
// 			fieldtype: "Select",
// 			options: "\nLow\nMedium\nHigh",
// 		},
// 	],
// };

console.log("hello");


console.log(document.getElementsByClassName("dataset-units"))


console.log("hello")



 let dataset=document.getElementsByClassName("dataset-units");
 console.log(dataset);


setTimeout(()=>{
    for(let i=0;i<4;i++){
        console.log("dfkj")
        dataset[i].addEventListener("click",(e)=>{
            // console.log(e.currentTarget)
            let element = e.currentTarget;
            console.log(element.classList);
            element_class = element.classList[2];
            console.log(element_class)

            if(element_class == "dataset-0"){
                window.location = "/app/project?custom_stage=Foundation"
            }
            else if(element_class == "dataset-1"){
                window.location = "/app/project?custom_stage=Erection"
            }
            else if(element_class == "dataset-2"){
                window.location = "/app/project?custom_stage=Stringing"
            }
            else if(element_class == "dataset-3"){
                window.location = "/app/project?custom_stage=Procurement"
            }

        })
     }
},2000)