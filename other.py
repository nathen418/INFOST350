def displayTemplate(template):
    # display the template contents

    print(f"Template Name: {template['template_name']}")
    print(f"Template Style: {template['template_style']}")
    print(f"Template Body: {template['template_body']}")
    print("The template you have chosen has the following variables")
    for variable in template['template_variables']:
        print(variable)
    
def fillInTemplate(template):
    # get the template variables
    templateVariables = template['template_variables']
    for variable in templateVariables:
        print(f"Please enter the {variable}")
        templateVariables[variable] = input()