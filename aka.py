import re

first_half = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>srp links</title>
</head>

<body>
    <div id='links'>
        <h3><a id='project_page' href='https://github.com/klawr/deepmech/tree/master/reports/srp'>Project Page</a></h3>
        <p>To be redirected via URL hash activate JavaScript</p>
        <ol>"""
	
second_half = """
        </ol>
    </div>

    <script>
        const hash = window.location.hash;
        let a;
        if (hash) {
            a = document.getElementById(hash);
        }
        if (!a) {
            a = document.getElementById('project_page')
        }
        if (a) {
            document.getElementById('links').style.display = 'none';
            const text = document.createElement('h3');
            text.innerHTML = `You are being redirected to: ${a.href}`;
            document.body.appendChild(text);
            setTimeout(() => { a.click(); }, 1000);
        }
    </script>
</body>

</html>
"""

aka_path = input('Path to .aka file: ')

def list_entry(id, url):
    return """
            <li>
                <a id='%s' href='%s'>
                    %s
                </a>
            </li>""" % (id, url, url)

aka = 'https://aka.klawr.de/'
def is_aka(string_list):
    chk = map(lambda string: aka in string, string_list)
    lst = list(chk)
    return all(lst)

with open(aka_path) as aka_file:
    aka = aka_file.read()
    ids = re.findall(r'{\\url\s*{\\(#\d+)}:', aka)
    url = re.findall(r'{\\url\s*{(https:\/\/\S[^}]+)}', aka)

    if (len(ids) != len(url)):
        print('aka identifier not valid in all urls')
        exit()

    h = first_half
    
    for i in range(len(ids)):
        h += list_entry(ids[i], url[i])

    h += second_half

    with open('index.html', 'w') as html:
        html.write(h)
	
