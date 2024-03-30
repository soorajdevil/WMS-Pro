from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from google.cloud import dialogflow
from google.oauth2 import service_account
from wms.models import Login, Signup, Add_buildings, Add_racks, Add_bin, Add_supervisor, Add_rows, Add_products, Add_employee

# Create your views here.



def add_supervisor(request):
     return render(request,"html/add-supervisor.html")


def warehouse_login(request):
    return render(request,"html/warehouse-login.html")

def supervisor_warehouse_login(request):
    return render(request,"html/supervisor/supervisor-warehouse-login.html")

def add_building(request):
    try:
        id = request.session['id']
        return render(request,"html/add-building.html")
    except:
        return render(request,"html/warehouse-login.html")

def home(request):
    try:
        id = request.session['id']
        return render(request,"html/home.html")
    except:
        return render(request,"html/warehouse-login.html")

def view_all_buildings(request):
    try:
        id = request.session['id']
        return render(request,"html/View-all-buildings.html")
    except:
        return render(request,"html/warehouse-login.html")

def add_rack(request):
    try:
        id = request.session['id']
        return render(request,"html/add-rack.html")
    except:
        return render(request,"html/warehouse-login.html")

def view_rack(request):
    try:
        id = request.session['id']
        return render(request,"html/view-rack.html")
    except:
        return render(request,"html/warehouse-login.html")

def header(request):
    return render(request,"html/header.html")

def supervisor_header(request):
    return render(request,"html/supervisor/supervisor-header.html")

def edit_user(request):
    id = request.GET.get('id')
    Obj1 = Signup.objects.get(id = id)
    Obj1.name = 'Rohit'
    Obj1.save()
    dict = {'Success' : 'Success'}
    return JsonResponse(dict)


def addbuilding_action(request):
    name = request.GET.get('name')
    area = request.GET.get('area')
    floor = request.GET.get('floor')
    identifier = request.GET.get('identifier')
    height = request.GET.get('height')
    structure = request.GET.get('structure')
    flooring = request.GET.get('flooring')
    add = Add_buildings(name = name, area = area, floor = floor, identifier = identifier, height = height, structure = structure, flooring = flooring)
    add.save()
    dict = {'success' : 'Building added successfully!!!'}
    #return JsonResponse(dict)
    return render(request,'html/add-building.html',dict)

def add_rack_action(request):
    dict = {'success' : 'Rack added successfully!!!', 'Error' : 'Building not found!!!'}
    id = request.POST.get('id')
    rack_name = request.POST.get('rack_name')
    weight = request.POST.get('weight')
    nof_bin = request.POST.get('nof_bin')
    width = request.POST.get('width')
    height = request.POST.get('height')
    length = request.POST.get('length')
    save_rack = Add_racks(building_id = Add_buildings.objects.get(id = id), rack_name = rack_name, weight = weight, nof_bins = nof_bin, width = width, height = height, length = length)
    save_rack.save()
    rack1 = Add_racks.objects.latest('id')
    for i in range(int(nof_bin)):
        save_bin = Add_bin(rack_id = rack1, length = length, width = width, height = height, weight = weight)
        save_bin.save()
    return render(request,'html/add-rack.html',dict)

def view_bin(request):
    try:
        id = request.session['id']
        return render(request,"html/view-bin.html")
    except:
        return render(request,"html/warehouse-login.html")

def view_bin_action(request):
    id = request.GET.get('id')
    view_all = Add_bin.objects.all()
    view = Add_bin.objects.filter(rack_id = id)
    list_id = []
    list_rack = []
    list_length = []
    list_weight = []
    list_width = []
    list_height = []
    for i in view:
        list_id.append(i.bin_id)
        list_rack.append(i.rack_id.id)
        list_length.append(i.length)
        list_weight.append(i.weight)
        list_width.append(i.width)
        list_height.append(i.height)
    dict = {'id' : list_id, 'rack_id' : list_rack, 'length' : list_length, 'weight' : list_weight, 'width' : list_width, 'height' : list_height}
    return JsonResponse(dict)
    #return render(request,'html/view-bin.html',dict)

def edit_bin(request):
    try:
        id = request.session['id']
        return render(request,"html/edit-bin.html")
    except:
        return render(request,"html/warehouse-login.html")

def edit_bin_action(request):
    id = request.GET.get('bin_id')
    load = Add_bin.objects.filter(bin_id = id)
    list_id = []
    list_rack = []
    list_rack_name = []
    list_length = []
    list_weight = []
    list_width = []
    list_height = []
    for i in load:
        list_id.append(i.bin_id)
        list_rack.append(i.rack_id.id)
        list_rack_name.append(i.rack_id.rack_name)
        list_length.append(i.length)
        list_weight.append(i.weight)
        list_width.append(i.width)
        list_height.append(i.height)
    dict = {'id' : i.bin_id, 'rack_id' : list_rack,'name': i.rack_id.rack_name, 'length' : list_length, 'weight' : list_weight, 'width' : list_width, 'height' : list_height}
    return render(request,'html/edit-bin.html',dict)

def edit_bin_action_save(request):
    id = request.POST.get('id')
    weight = request.POST.get('weight')
    width = request.POST.get('width')
    height = request.POST.get('height')
    length = request.POST.get('length')
    load = Add_bin.objects.get(bin_id = id)
    if weight != "" and height !="" and length !="" and width != "":
        load.weight = weight
        load.height = height
        load.length = length
        load.width = width
        load.save()
        dict = {'success' : 'Updated successfully'}
        return render(request,"html/view-bin.html",dict)
    else:
        dict = {'error' : 'values cannot be null!!!'}
        return render(request,"html/edit-bin.html",dict)


def view_building(request):
    view_building = Add_buildings.objects.all()
    dict = {}
    id = []
    list_name = []
    list_area = []
    list_floor = []
    list_identifier  = []
    list_height = []
    list_structure = []
    list_flooring = []
    for i in view_building:
        id.append(i.id)
        list_name.append(i.name)
        list_area.append(i.area)
        list_floor.append(i.floor)
        list_identifier.append(i.identifier)
        list_height.append(i.height)
        list_structure.append(i.structure)
        list_flooring.append(i.flooring)
    dict = {'id': id, 'name' : list_name, 'area' : list_area, 'floor' : list_floor, 'identifier' : list_identifier, 'height' : list_height, 'structure' : list_structure, 'flooring' : list_flooring}
    return JsonResponse(dict)

def view_rack_action(request):
    id = request.GET.get('id')
    view_all_rack = Add_racks.objects.all()
    view_rack = Add_racks.objects.filter(building_id = id)
    dict = {}
    id = []
    building_id = []
    list_name = []
    list_weight = []
    list_nof_bins = []
    list_width = []
    list_height = []
    list_length = []
    for i in view_rack:
        id.append(i.id)
        building_id.append(i.building_id.id)
        list_name.append(i.rack_name)
        list_weight.append(i.weight)
        list_nof_bins.append(i.nof_bins)
        list_width.append(i.width)
        list_height.append(i.height)
        list_length.append(i.length)
    dict ={'rack_id': id, 'building_id' : building_id, 'name': list_name, 'weight': list_weight, 'nof_bin' : list_nof_bins, 'width' : list_width, 'height' : list_height, 'length' : list_length}
    return JsonResponse(dict)

def delete(request):
    id = 8
    # obj = Add_supervisor.objects.get(supervisor_id = str(id))
    # obj.delete()
    for i in range(2,13):
      obj = Add_employee.objects.get(employee_id = str(i))
      obj.delete()
    return HttpResponse('success')

def warehouse_login_action(request):
    flag = False
    name = request.GET.get('name')
    password = request.GET.get('password')
    select = Login.objects.all()
    for i in select:
        if name == i.username and password == i.password:
            flag = True
            break
    if flag == True:
        request.session['id'] = 1
        return render(request,'html/home.html')
    else:
        return render(request,'html/warehouse-login.html')

def supervisor_warehouse_login_action(request):
    flag = False
    email = request.GET.get('name')
    password = request.GET.get('password')
    select = Add_supervisor.objects.all()
    for i in select:
        if i.email == email and i.ssn == int(password):
            flag = True
            id = i.supervisor_id
            break
    if flag == True:
        request.session['id'] = id
        return render(request,'html/supervisor/supervisor-home.html')
    else:
        return render(request,'html/supervisor/supervisor-warehouse-login.html')

def warehouse_logout_action(request):
    try:
        del request.session['id']
    except:
        pass
    return render(request,'html/warehouse-login.html')

def supervisor_warehouse_logout_action(request):
    try:
        del request.session['id']
    except:
        pass
    return render(request,'html/supervisor/supervisor-warehouse-login.html')

def supervisor_home(request):
    try:
        id = request.session['id']
        return render(request,"html/supervisor/supervisor-home.html")
    except:
        return render(request,"html/supervisor-warehouse-login.html")

def edit_building(request):
    try:
        id = request.session['id']
        return render(request,"html/edit-building.html")
    except:
        return render(request,"html/warehouse-login.html")

def edit_building_action(request):
    id = request.GET.get('id')
    edit_building = Add_buildings.objects.filter(id = id)
    dict = {}
    id = []
    list_name = []
    list_area = []
    list_floor = []
    list_identifier  = []
    list_height = []
    list_structure = []
    list_flooring = []
    for i in edit_building:
        id.append(i.id)
        list_name.append(i.name)
        list_area.append(i.area)
        list_floor.append(i.floor)
        list_identifier.append(i.identifier)
        list_height.append(i.height)
        list_structure.append(i.structure)
        list_flooring.append(i.flooring)
    dict = {'id': id, 'name' : list_name, 'area' : list_area, 'floor' : list_floor, 'identifier' : list_identifier, 'height' : list_height, 'structure' : list_structure, 'flooring' : list_flooring}
    return JsonResponse(dict)

def edit_building_action_save(request):
    id = request.GET.get('id')
    name = request.GET.get('name')
    area = request.GET.get('area')
    floor = request.GET.get('floor')
    identifier = request.GET.get('identifier')
    height = request.GET.get('height')
    structure = request.GET.get('structure')
    flooring = request.GET.get('flooring')
    edit = Add_buildings.objects.get(id = id)
    edit.name = name
    edit.area = area
    edit.floor = floor
    edit.identifier = identifier
    edit.height = height
    edit.structure = structure
    edit.flooring = flooring
    edit.save()
    return HttpResponse('Updated successfully!!!')

def edit_rack(request):
    try:
        id = request.session['id']
        return render(request,"html/edit-rack.html")
    except:
        return render(request,"html/warehouse-login.html")

def edit_rack_action(request):
    id = request.GET.get('id')
    edit_rack = Add_racks.objects.filter(id = id)
    dict = {}
    id = []
    building_id = []
    list_name = []
    list_weight = []
    list_nof_bins = []
    list_width = []
    list_height = []
    list_length = []
    for i in edit_rack:
        id.append(i.id)
        building_id.append(i.building_id.id)
        list_name.append(i.rack_name)
        list_weight.append(i.weight)
        list_nof_bins.append(i.nof_bins)
        list_width.append(i.width)
        list_height.append(i.height)
        list_length.append(i.length)
    dict ={'rack_id': id, 'building_id' : building_id, 'name': list_name, 'weight': list_weight, 'nof_bin' : list_nof_bins, 'width' : list_width, 'height' : list_height, 'length' : list_length}
    return JsonResponse(dict)

def edit_rack_action_save(request):
    id = request.GET.get('id')
    rack_name = request.GET.get('rack_name')
    weight = request.GET.get('weight')
    nof_bin = request.GET.get('nof_bin')
    width = request.GET.get('width')
    height = request.GET.get('height')
    length = request.GET.get('length')
    edit = Add_racks.objects.get(id = id)
    edit.name = rack_name
    edit.weight = weight
    edit.nof_bins = nof_bin
    edit.width = width
    edit.height = height
    edit.length = length
    edit.save()
    dict = {'success' : 'Updated successfully'}
    return render(request,'html/edit-rack.html',dict)

def add_supervisor(request):
    try:
        id = request.session['id']
        return render(request,"html/add-supervisor.html")
    except:
        return render(request,"html/warehouse-login.html")

def add_supervisor_action(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    phone = request.GET.get('phone')
    address = request.GET.get('address')
    ssn = request.GET.get('ssn')
    add = Add_supervisor(name = name, email = email, phone = phone, address = address, ssn = ssn)
    add.save()
    dict = {'success' : 'Supervisor added successfully'}
    return render(request,'html/add-supervisor.html',dict)

def view_supervisor(request):
    try:
        id = request.session['id']
        return render(request,"html/view-supervisor.html")
    except:
        return render(request,"html/warehouse-login.html")

def view_supervisor_action(request):
    view = Add_supervisor.objects.all()
    list_id = []
    list_name = []
    list_email = []
    list_phone = []
    list_address = []
    list_ssn = []
    for i in view:
        list_id.append(i.supervisor_id)
        list_name.append(i.name)
        list_email.append(i.email)
        list_phone.append(i.phone)
        list_address.append(i.address)
        list_ssn.append(i.ssn)
    dict = {'id' : list_id, 'name' : list_name, 'email' : list_email, 'phone' : list_phone, 'address' : list_address, 'ssn' : list_ssn}
    return JsonResponse(dict)

def add_row(request):
    try:
        id = request.session['id']
        return render(request,"html/add-row.html")
    except:
        return render(request,"html/warehouse-login.html")

def add_row_action(request):
    rack_id = request.GET.get('rack_id')
    building_id = request.GET.get('building_id')
    name = request.GET.get('row_name')
    weight = request.GET.get('weight')
    width = request.GET.get('width')
    height = request.GET.get('height')
    length = request.GET.get('length')
    add = Add_rows(building_id = Add_buildings.objects.get(id = building_id), rack_id = Add_racks.objects.get(id = rack_id) ,name = name, weight = weight, width = width, height = height, length = length)
    add.save()
    dict = {'success' : 'Row added successfully'}
    return render(request,'html/add-row.html',dict)

def view_rows_action(request):
    view_all_rows= Add_rows.objects.all()
    #view_rack = Add_rows.objects.filter(building_id = id)
    dict = {}
    id = []
    building_id = []
    rack_id = []
    list_name = []
    list_weight = []
    list_nof_bins = []
    list_width = []
    list_height = []
    list_length = []
    for i in view_all_rows:
        id.append(i.id)
        building_id.append(i.building_id.id)
        rack_id.append(i.rack_id.id)
        list_name.append(i.name)
        list_weight.append(i.weight)
        list_width.append(i.width)
        list_height.append(i.height)
        list_length.append(i.length)
    dict ={'id': id,'rack_id': id, 'building_id' : building_id, 'name': list_name, 'weight': list_weight, 'width' : list_width, 'height' : list_height, 'length' : list_length}
    return JsonResponse(dict)

def supervisor_add_product(request):
    try:
        id = request.session['id']
        return render(request,"html/supervisor/supervisor-add-product.html")
    except:
        return render(request,"html/supervisor/supervisor-warehouse-login.html")

def supervisor_add_product_action(request):
    load = Add_products.objects.all()
    name = request.GET.get('name')
    brand = request.GET.get('brand')
    model = request.GET.get('model')
    quantity = request.GET.get('quantity')
    weight = request.GET.get('weight')
    length = request.GET.get('length')
    width = request.GET.get('width')
    height = request.GET.get('height')
    if name != "" and brand != "" and model !="" and quantity !="" and weight !="" and length !="" and width !="" and height != "":
        add = Add_products(name = name, brand = brand, model = model, quantity = quantity, weight = weight,length = length, Width = width, height = height)
        add.save()
        dict = {'success' : 'Product added successfully'}
        return render(request,"html/supervisor/supervisor-add-product.html",dict)
    else:
        dict = {'error' : 'values cannot be null!!!'}
        return render(request,"html/supervisor/supervisor-add-product.html",dict)

def supervisor_view_product(request):
    try:
        id = request.session['id']
        return render(request,"html/supervisor/supervisor-view-products.html")
    except:
        return render(request,"html/supervisor/supervisor-warehouse-login.html")

def supervisor_view_procducts_action(request):
    id = request.session['id']
    view_name = Add_supervisor.objects.filter(supervisor_id = id)
    load = Add_products.objects.all()
    supervisor =[]
    for i in view_name:
        supervisor.append(i.name)
    list_id = []
    list_name = []
    list_brand = []
    list_model = []
    list_quantity = []
    list_weight = []
    list_length = []
    list_width = []
    list_height = []
    for i in load:
        list_id.append(i.product_id)
        list_name.append(i.name)
        list_brand.append(i.brand)
        list_model.append(i.model)
        list_quantity.append(i.quantity)
        list_weight.append(i.weight)
        list_length.append(i.length)
        list_width.append(i.Width)
        list_height.append(i.height)
    dict = {'supervisor': supervisor,'id': list_id,'name' : list_name, 'brand' : list_brand, 'model' : list_model, 'quantity' : list_quantity, 'weight' : list_weight, 'length' : list_length, 'width' : list_width, 'height' : list_height}
    return JsonResponse(dict)

def supervisor_delete_product(request):
    id = request.GET.get('id')
    load = Add_products.objects.filter(product_id = id)
    load.delete()
    dict = {'success' :'Product deleted successfully'}
    return render(request,"html/supervisor/supervisor-view-products.html",dict)

def supervisor_edit_product(request):
    try:
        id = request.session['id']
        return render(request,"html/supervisor/supervisor-edit-product.html")
    except:
        return render(request,"html/supervisor/supervisor-warehouse-login.html")

def supervisor_edit_product_action(request):
    product_id = request.GET.get('product_id')
    load = Add_products.objects.filter(product_id = product_id)
    list_id = []
    list_name = []
    list_brand = []
    list_model = []
    list_quantity = []
    list_weight = []
    list_length = []
    list_width = []
    list_height = []
    for i in load:
        dict = {'product_id': i.product_id,'name' : i.name, 'brand' : i.brand, 'model' : i.model, 'quantity' : i.quantity, 'weight' : i.weight, 'length' : i.length, 'width' : i.Width, 'height' : i.height}
    return render(request,"html/supervisor/supervisor-edit-product.html",dict)

def supervisor_edit_product_action_save(request):
    id = request.GET.get('product_id')
    edit = Add_products.objects.get(product_id = id)
    name = request.GET.get('name')
    brand = request.GET.get('brand')
    model = request.GET.get('model')
    quantity = request.GET.get('quantity')
    weight = request.GET.get('weight')
    length = request.GET.get('length')
    width = request.GET.get('width')
    height = request.GET.get('height')
    if name != "" and brand != "" and model !="" and quantity !="" and weight !="" and length !="" and width !="" and height != "":
        edit.name = name
        edit.brand = brand
        edit.model = model
        edit.quantity = quantity
        edit.weight = weight
        edit.length = length
        edit.width = width
        edit.height = height
        edit.save()
        dict = {'success' : 'Updated successfully'}
        return render(request,"html/supervisor/supervisor-view-products.html",dict)
    else:
        dict = {'error' : 'values cannot be null!!!'}
        return render(request,"html/supervisor/supervisor-edit-product.html",dict)

def supervisor_add_box(request):
    try:
        id = request.session['id']
        return render(request,"html/supervisor/supervisor-add-box.html")
    except:
        return render(request,"html/supervisor/supervisor-warehouse-login.html")

def supervisor_add_box_action(request):
    pass

def add_employee(request):
    try:
        id = request.session['id']
        return render(request,"html/add-employee.html")
    except:
        return render(request,"html/warehouse-login.html")

def view_employee(request):
    try:
        id = request.session['id']
        return render(request,"html/view-employee.html")
    except:
        return render(request,"html/warehouse-login.html")

def edit_employee(request):
    try:
        id = request.session['id']
        return render(request,"html/edit-employee.html")
    except:
        return render(request,"html/warehouse-login.html")

def add_employee_action(request):
    name = request.GET.get('name')
    phone = request.GET.get('phone')
    address = request.GET.get('address')
    ssn = request.GET.get('ssn')
    tin = request.GET.get('tin')
    employee_type = request.GET.get('employee_type')
    add = Add_employee(name = name, phone = phone, address = address, ssn = ssn,tin =tin, employee_type = employee_type)
    add.save()
    dict = {'success' : 'Employee added successfully'}
    return render(request,"html/add-employee.html",dict)

def view_employee_action(request):
    view = Add_employee.objects.all()
    list_id = []
    list_name = []
    list_phone = []
    list_address = []
    list_ssn = []
    list_tin = []
    list_employee_type = []
    for i in view:
        list_id.append(i.employee_id)
        list_name.append(i.name)
        list_phone.append(i.phone)
        list_address.append(i.address)
        list_ssn.append(i.ssn)
        list_tin.append(i.tin)
        list_employee_type.append(i.employee_type)
    dict = {'id' : list_id, 'name' : list_name, 'phone' : list_phone, 'address' : list_address, 'ssn' : list_ssn,'tin' : list_tin, 'type' : list_employee_type}
    return JsonResponse(dict)

def edit_employee_action(request):
    id = request.GET.get('employee_id')
    load = Add_employee.objects.filter(employee_id = id)
    dict = {}
    for i in load:
        dict = {'employee_id' : i.employee_id, 'name' : i.name, 'phone' : i.phone, 'address' : i.address, 'ssn' : i.ssn,'tin' : i.tin}
    return render(request,"html/edit-employee.html",dict)

def edit_employee_action_save(request):
    employee_id = request.GET.get('employee_id')
    name = request.GET.get('name')
    phone = request.GET.get('phone')
    address = request.GET.get('address')
    ssn = request.GET.get('ssn')
    tin = request.GET.get('tin')
    employee_type = request.GET.get('employee_type')
    load = Add_employee.objects.get(employee_id = employee_id)
    load.name = name
    load.phone = phone
    load.address = address
    load.ssn = ssn
    load.tin = tin
    load.employee_type = employee_type
    load.save()
    dict = {'success' : True}
    return render(request,"html/view-employee.html",dict)

def supervisor_view_box(request):
    try:
        id = request.session['id']
        return render(request,"html/supervisor/supervisor-view-box.html")
    except:
        return render(request,"html/supervisor/supervisor-warehouse-login.html")

def supervisor_add_employee_attendence(request):
    try:
        id = request.session['id']
        return render(request,"html/supervisor/supervisor-add-employee-attendence.html")
    except:
        return render(request,"html/supervisor/supervisor-warehouse-login.html")

def supervisor_view_employee(request):
    try:
        id = request.session['id']
        return render(request,"html/supervisor/supervisor-view-employee-detail.html")
    except:
        return render(request,"html/supervisor/supervisor-warehouse-login.html")
def supervisor_box_transit(request):
    try:
        id = request.session['id']
        return render(request,"html/supervisor/supervisor-box-transit.html")
    except:
        return render(request,"html/supervisor/supervisor-warehouse-login.html")

def supervisor_view_employee_attendence(request):
    try:
        id = request.session['id']
        return render(request,"html/supervisor/supervisor-view-employee-attendence.html")
    except:
        return render(request,"html/supervisor/supervisor-warehouse-login.html")

def supervisor_view_rack_report(request):
    try:
        id = request.session['id']
        return render(request,"html/supervisor/supervisor-view-rack-report.html")
    except:
        return render(request,"html/supervisor/supervisor-warehouse-login.html")

def supervisor_free_space(request):
    try:
        id = request.session['id']
        return render(request,"html/supervisor/supervisor-free-space.html")
    except:
        return render(request,"html/supervisor/supervisor-warehouse-login.html")

def job_sheduling(request):
    try:
        id = request.session['id']
        return render(request,"html/job-sheduling.html")
    except:
        return render(request,"html/warehouse-login.html")

def view_product(request):
    try:
        id = request.session['id']
        return render(request,"html/view-product.html")
    except:
        return render(request,"html/warehouse-login.html")

def manager_view_product(request):
    name = request.GET.get('name')
    load = Add_products.objects.filter(name=name)
    list_name = []
    list_brand = []
    list_quantity = []
    count = 0
    for i in load:
        list_name.append(i.name)
        list_brand.append(i.brand)
        list_quantity.append(i.quantity)
        count = count + 1
    dict = {'count': count,'name': list_name, 'brand': list_brand, 'quantity': list_quantity}
    return JsonResponse(dict)

def supervisor_view_employee_action(request):
    ssn = request.GET.get('ssn')
    load = Add_employee.objects.get(ssn = ssn)
    dict = {'name' : load.name, 'phone' : load.phone, 'address' : load.address, 'ssn' : load.ssn, 'tin' : load.tin, 'employee-type' : load.employee_type}
    return JsonResponse(dict)

def chatbotdemo(request):
    return render(request,"html/chatbotdemo.html")

def detect_intent_texts(request):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    project_id = "lmcinterntest-qrjy"
    session_id = 1
    language_code = "en-IN"
    texts = [request.GET.get('text')]
    CREDENTIALS = service_account.Credentials.from_service_account_file("C:/Users/ramch/django_project/warehouse/wms/static/json/chatbot.json")

    session_client = dialogflow.SessionsClient(credentials=CREDENTIALS)

    session = session_client.session_path(project_id, session_id)
    print("Session path: {}\n".format(session))

    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        print("=" * 20)
        print("Query text: {}".format(response.query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
            )
        )
        print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))
    dict = {'name': response.query_result.intent.display_name, 'result': response.query_result.fulfillment_text}
    return JsonResponse(dict)

def chat_free_space(request):
    result = 2055
    dict = {'result' : result}
    return JsonResponse(dict)

def chat_employee_present(request):
    result = 15
    dict = {'result' : result}
    return JsonResponse(dict)

def chat_employee_absent(request):
    result = 200
    dict = {'result' : result}
    return JsonResponse(dict)

def chat_employee_details(request):
    ssn = request.GET.get('ssn')
    load = Add_employee.objects.get(ssn = ssn)
    dict = {'name' : load.name, 'phone' : load.phone, 'address': load.address, 'ssn' : load.ssn, 'tin' : load.tin, 'employee-type' : load.employee_type}
    return JsonResponse(dict)

def chat_supervisor_details(request):
    ssn = request.GET.get('ssn')
    load = Add_supervisor.objects.get(ssn = ssn)
    dict = {'name' : load.name, 'phone' : load.phone, 'address': load.address, 'ssn' : load.ssn, 'email' : load.email}
    return JsonResponse(dict)
