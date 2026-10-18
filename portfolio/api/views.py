from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

# Create your views here.

class AboutView(View):
    def get(self,request):
        data = {
            "id" : "A101",
            "Full Name" : "Anu Tom",
            "Professional Title" : "Software Engineer",
            "Bio" : "Passionate Coder",
            "DOB" : "19-02-1990",
            "Email" : "anutom19@gmail.com",
            "Contact Number" : 987654321,
            "Location" : "New Zealand",
            "GitHub URL" : "abcdefg",
            "LinkedLn URL" : "hijklmnop"
        }
        return JsonResponse(data)


class EducationView(View):
    def get(self,request):
        data = {
            "id" : "E101",
            "Institution" : "AJCE",
            "Degree" : "B.Tech",
            "University" : "MG University",
            "Location" : "Kerala",
            "Start Year" : 2009,
            "End year" : 2013,
            "CGPA" : 6.7,
            "Description" : "B.Tech in Information Technology"
        }
        return JsonResponse(data)

class ProjectsView(View):
    def get(self,request):
        projects = [
            {
                "id" : 1,
                "title" : "Picture Password",
                "short description": "Picture Passwords",
                "long description" : "Picture Passwords for added security",
                "technologies used" : ["Python","Django","HTML"],
                "live url" : "abc",
                "images url" : "def",
                "github url" : "ghi",
                "featured" : True
            },
            {
                "id" : 2,
                "title" : "AI and Machine Learning",
                "short description": "AI and Machine Learning",
                "long description" : "AI and Machine Learning for advanced automation",
                "technologies used" : ["Python","Django","HTML"],
                "live url" : "jkl",
                "images url" : "mno",
                "github url" : "pqr",
                "featured" : True
            },
                        {
                "id" : 3,
                "title" : "Web Scrapping",
                "short description": "Web Scrapping",
                "long description" : "Web Scrapping for huge tons of data",
                "technologies used" : ["Python","Django","HTML"],
                "live url" : "stu",
                "images url" : "vwx",
                "github url" : "yza",
                "featured" : True
            }
        ]
        return JsonResponse(projects,safe = False)

class SkillsView(View):
    def get(self,request):
        skills = [
            {
                "id" : 1,
                "skill name" : "Python",
                "category" : "Programming Language",
                "proficiency" : "Advanced",
                "years of experience" : 2
            },
            {
                "id" : 2,
                "skill name" : "Django",
                "category" : "Backend",
                "proficiency" : "Advanced",
                "years of experience" : 1
            },
            {
                "id" : 3,
                "skill name" : "React",
                "category" : "FrontEnd",
                "proficiency" : "Advanced",
                "years of experience" : 2
            }
        ]
        return JsonResponse(skills,safe = False)

class ExperienceView(View):
    def get(self,request):
        experience = [
            {
                "id" : 1,
                "Job Title" : "Programmer Analyst",
                "Company Name" : "CTS",
                "Location" : "Coimbatore",
                "Employment Type" : "Permanent",
                "Start Date" : "2014",
                "End Date" : "2016",
                "Currently Working" : "Luminar",
                "Description" : "Worked as a programmer analyst at CTS"
            },
            {
                "id" : 2,
                "Job Title" : "Associate",
                "Company Name" : "CTS",
                "Location" : "Kochi",
                "Employment Type" : "Permanent",
                "Start Date" : "2017",
                "End Date" : "2020",
                "Currently Working" : "Luminar",
                "Description" : "Worked as an associate at CTS"
            }
        ]
        return JsonResponse(experience, safe = False)


class CertificationView(View):
    def get(self,request):
        certificates = [
            {
                "id" : 1,
                "certification name" : "Python Developer",
                "issuing organization" : "Python Org",
                "issued date" : "2017"
            },
            {
                "id" : 2,
                "certification name" : "Python Developer Advanced",
                "issuing organization" : "Python Org",
                "issued date" : "2019"
            }
        ]
        return JsonResponse(certificates, safe = False)


class ServiceView(View):
    def get(self,request):
        services = [
            {
                "id" : 1,
                "service name" : "Web Development",
                "description" : "Expert in web Development",
                "technologies" : ["Python","Django","HTML"],
            },
            {
                "id" : 2,
                "service name" : "Web Scrapping",
                "description" : "Expert in web Scrapping",
                "technologies" : ["Python","Django","HTML"],
            }
        ]
        return JsonResponse(services, safe = False)
    
