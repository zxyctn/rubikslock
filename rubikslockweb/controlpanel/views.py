import json
from pathlib import Path

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt

from controlpanel.main import get_cube, solve_cube, compare_solutions

def index(request):
    return render(request, "index.html")

def upload(request):
    if request.method == 'POST':        
        print(request.FILES)

        reference_f = request.FILES['reference_f']
        reference_r = request.FILES['reference_r']
        reference_b = request.FILES['reference_b']
        reference_l = request.FILES['reference_l']
        reference_t = request.FILES['reference_t']
        reference_d = request.FILES['reference_d']

        solved_f = request.FILES['solved_f']
        solved_r = request.FILES['solved_r']
        solved_b = request.FILES['solved_b']
        solved_l = request.FILES['solved_l']
        solved_t = request.FILES['solved_t']
        solved_d = request.FILES['solved_d']

        fss = FileSystemStorage()
        # file_reference_f = fss.save(reference_f.name, reference_f)
        # file_reference_r = fss.save(reference_r.name, reference_r)
        # file_reference_b = fss.save(reference_b.name, reference_b)
        # file_reference_l = fss.save(reference_l.name, reference_l)
        # file_reference_t = fss.save(reference_t.name, reference_t)
        # file_reference_d = fss.save(reference_d.name, reference_d)

        # file_solved_f = fss.save(solved_f.name, solved_f)
        # file_solved_r = fss.save(solved_r.name, solved_r)
        # file_solved_b = fss.save(solved_b.name, solved_b)
        # file_solved_l = fss.save(solved_l.name, solved_l)
        # file_solved_t = fss.save(solved_t.name, solved_t)
        # file_solved_d = fss.save(solved_d.name, solved_d)

        file_reference_f = fss.save("reference_f.jpeg", reference_f)
        file_reference_r = fss.save("reference_r.jpeg", reference_r)
        file_reference_b = fss.save("reference_b.jpeg", reference_b)
        file_reference_l = fss.save("reference_l.jpeg", reference_l)
        file_reference_t = fss.save("reference_t.jpeg", reference_t)
        file_reference_d = fss.save("reference_d.jpeg", reference_d)

        file_solved_f = fss.save("solved_f.jpeg", solved_f)
        file_solved_r = fss.save("solved_r.jpeg", solved_r)
        file_solved_b = fss.save("solved_b.jpeg", solved_b)
        file_solved_l = fss.save("solved_l.jpeg", solved_l)
        file_solved_t = fss.save("solved_t.jpeg", solved_t)
        file_solved_d = fss.save("solved_d.jpeg", solved_d)


        file_reference_f_url = fss.url(file_reference_f)
        file_reference_r_url = fss.url(file_reference_r)
        file_reference_b_url = fss.url(file_reference_b)
        file_reference_l_url = fss.url(file_reference_l)
        file_reference_t_url = fss.url(file_reference_t)
        file_reference_d_url = fss.url(file_reference_d)

        file_solved_f_url = fss.url(file_solved_f)
        file_solved_r_url = fss.url(file_solved_r)
        file_solved_b_url = fss.url(file_solved_b)
        file_solved_l_url = fss.url(file_solved_l)
        file_solved_t_url = fss.url(file_solved_t)
        file_solved_d_url = fss.url(file_solved_d)

        base_path = str(Path(__file__).resolve().parent.parent)
        base_path = base_path.replace("\\", "/")

        reference_cube = get_cube(
            base_path + file_reference_f_url,
            base_path + file_reference_r_url,
            base_path + file_reference_b_url,
            base_path + file_reference_l_url,
            base_path + file_reference_t_url,
            base_path + file_reference_d_url
        )

        print("Reference: ///////////////////////////////////////////////////////////////////")
        print(reference_cube)
        print("/////////////////////////////////////////////////////////////////////")

        solution = solve_cube(get_password(), reference_cube.copy())

        solved_cube = get_cube(
            base_path + file_solved_f_url,
            base_path + file_solved_r_url,
            base_path + file_solved_b_url,
            base_path + file_solved_l_url,
            base_path + file_solved_t_url,
            base_path + file_solved_d_url
        )

        print("Solution: *********************************************************************")
        print(solution)
        print("*********************************************************************")

        is_same = compare_solutions(solution, solved_cube)

        print("Solved: =======================================================================")
        print(solved_cube)
        print("=====================================================================")

        fss.delete(base_path + file_reference_f_url)
        fss.delete(base_path + file_reference_r_url)
        fss.delete(base_path + file_reference_b_url)
        fss.delete(base_path + file_reference_l_url)
        fss.delete(base_path + file_reference_t_url)
        fss.delete(base_path + file_reference_d_url)

        fss.delete(base_path + file_solved_f_url)
        fss.delete(base_path + file_solved_r_url)
        fss.delete(base_path + file_solved_b_url)
        fss.delete(base_path + file_solved_l_url)
        fss.delete(base_path + file_solved_t_url)
        fss.delete(base_path + file_solved_d_url)

        return render(
            request,
            "access_granted.html"
            if is_same
            else
            "access_denied.html"
        )

def new(request):
    return render(request, "access_granted.html")

@csrf_exempt
def set_password(request):
    data = json.loads(request.body)

    data["old"] = data["old"].upper()
    data["new"] = data["new"].upper()

    password = get_password()
    print(password)
    print(data["old"])

    base_path = str(Path(__file__).resolve().parent.parent)
    base_path = base_path.replace("\\", "/")

    if (password == data["old"]):
        f = open(base_path + '/controlpanel/pass.txt', "w")
        f.write(data["new"])
        f.close()
    print ("Password changed" if data["old"] == password else "Entered password is wrong")
    return HttpResponse(status=200 if data["old"] == password else 404)

def get_password():
    password = ""

    base_path = str(Path(__file__).resolve().parent.parent)
    base_path = base_path.replace("\\", "/")

    with open(base_path + '/controlpanel/pass.txt') as f:
        password = f.readlines()
    
    return password[0]
