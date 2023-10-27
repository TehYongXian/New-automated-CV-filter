from django.shortcuts import render
from django.http import HttpResponse
import re

def landing_page(request):
    return render(request, 'landing_page.html')


def read_file(request):
    # print("it work")
    # f = open('doc/fake_CV.txt', 'r')
    # file_content = f.read()
    # f.close()
    if request.method == 'POST' and request.FILES['uploaded_file']:
        uploaded_file = request.FILES['uploaded_file']
        file_content = uploaded_file.read().decode('utf-8')

    filtered_data = filter_text(file_content)

    context = {'file_content': file_content, **filtered_data }
    return render(request, "displayTXT.html", context)


def filter_text(file_content):
    programming_languages = ["Python", "Java", "C\+\+", "C", "C\#", "JavaScript", "Ruby", "PHP", "Swift", "TypeScript", "Go", "Rust", "Perl"]
    database_management = ["SQL", "MySQL", "PostgreSQL", "MongoDB", "Oracle", "Redis", "Cassandra", "Couchbase", "SQLite", "MariaDB", "Amazon DynamoDB", "Microsoft Azure Cosmos DB"]
    web_development = ["HTML", "CSS", "JavaScript", "React", "Angular", "Vue", "Node.js", "Ruby", "Express.js", "Laravel"]
    artificial_intelligence = ["AI", "Deep Learning", "Neural Networks", "NLP"]
    mobile_development = ["iOS", "Android", "Swift", "Kotlin"]
    operating_systems = ["Windows", "Linux", "macOS"]
    hobbies = ["Hiking", "Photography", "Videography","Cooking", "Gardening", "Painting", "Cycling", "Singing", "Dancing", "Fishing", 
               "Yoga", "Reading", "Traveling", "Swimming", "Gaming",  "Golf", "Knitting", "Meditation", "Camping"]

    programming_languages = [re.escape(keyword) for keyword in programming_languages]
    database_management = [re.escape(keyword) for keyword in database_management]
    web_development = [re.escape(keyword) for keyword in web_development]
    artificial_intelligence = [re.escape(keyword) for keyword in artificial_intelligence]
    mobile_development = [re.escape(keyword) for keyword in mobile_development]
    operating_systems = [re.escape(keyword) for keyword in operating_systems]
    hobbies = [re.escape(keyword) for keyword in hobbies]

    programming_languages_regex = re.compile(r'\b(?:' + '|'.join(programming_languages) + r')\b', re.I)
    database_management_regex = re.compile(r'\b(?:' + '|'.join(database_management) + r')\b', re.I)
    web_development_regex = re.compile(r'\b(?:' + '|'.join(web_development) + r')\b', re.I)
    ai_regex = re.compile(r'\b(?:' + '|'.join(artificial_intelligence) + r')\b', re.I)
    mobile_dev_regex = re.compile(r'\b(?:' + '|'.join(mobile_development) + r')\b', re.I)
    os_regex = re.compile(r'\b(?:' + '|'.join(operating_systems) + r')\b', re.I)
    hobbies_regex = re.compile(r'\b(?:' + '|'.join(hobbies) + r')\b', re.I)



    programming_languages_matches = set(programming_languages_regex.findall(file_content))
    database_management_matches = set(database_management_regex.findall(file_content))
    web_development_matches = set(web_development_regex.findall(file_content))
    ai_matches = set(ai_regex.findall(file_content))
    mobile_dev_matches = set(mobile_dev_regex.findall(file_content))
    os_matches = set(os_regex.findall(file_content))
    hobbies_matches = set(hobbies_regex.findall(file_content))


    return {
        'programming_languages': programming_languages_matches,
        'database_management': database_management_matches,
        'web_development': web_development_matches,
        'artificial_intelligence': ai_matches,
        'mobile_development': mobile_dev_matches,
        'operating_systems': os_matches,
        'hobbies': hobbies_matches,
    }


def upload(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file_upload']
        if uploaded_file.name.endswith('.txt'):
            # Read the uploaded file content
            file_content = uploaded_file.read().decode('utf-8')
            
            # Filter the content
            filtered_data = filter_text(file_content)

            context = {
                'file_content': file_content,
                **filtered_data  # Unpack the filtered data into the context
            }
            
            return render(request, "displayTXT.html", context)
        else:
            return HttpResponse("Please upload a valid .txt file.")
    else:
        return render(request, "uploadFile.html")