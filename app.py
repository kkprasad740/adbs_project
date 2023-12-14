from bottle import route, post, run, template, redirect, request
import database

# Call set_up_database to create tables and insert sample data
database.set_up_database()

@route("/")
def get_index():
    redirect("/list")

@route("/list")
def get_list():
    # Fetch data from both tables
    items_table1 = database.get_table1_data()
    items_table2 = database.get_table2_data()
    return template("list.tpl", data_table1=items_table1, data_table2=items_table2)

@route("/add")
def get_add():
    return template("add_course_student.tpl")

@post("/add")
def post_add():
    item_type = request.forms.get("item_type")
    item_count = request.forms.get("item_count")

    # Add item to the appropriate table
    if item_type in ["fruits", "vegetables", "powders"]:
        database.add_to_table1(item_type)
    else:
        database.add_to_table2(item_type, item_count)

    redirect("/list")

@route("/update/<id>")
def get_update(id):
    # Retrieve data from the appropriate table
    item_table1 = database.get_from_table1(id)
    item_table2 = database.get_from_table2(id)

    # Decide which template to use based on the table
    if item_table1:
        return template("update_course_student.tpl", item=item_table1[0])
    elif item_table2:
        return template("update_course_student.tpl", item=item_table2[0])
    else:
        redirect("/list")

@post("/update")
def post_update():
    item_type = request.forms.get("item_type")
    item_count = request.forms.get("item_count")
    id = request.forms.get("id")

    # Update item in the appropriate table
    if item_type in ["fruits", "vegetables", "powders"]:
        database.update_table1(id, item_type)
    else:
        database.update_table2(id, item_type, item_count)

    redirect("/list")

@route("/delete/<id>")
def get_delete(id):
    # Delete item from the appropriate table
    database.delete_item(id)
    redirect("/list")

run(host='localhost', port=8080)
