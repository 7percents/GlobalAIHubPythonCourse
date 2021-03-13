# Explain your work
# I created 5 CVs as dictionaries and merged them into a single list called 'cvs'. Finally, I printed all 5 CVs on screen.

# Homework 2
alan_cv = {
    'Name':'Alan',
    'Surname':'Turing',
    'Job Title':'Computer Scientist & Mathematician',
    'Contact Information': {
        'Phone': 4407700221197,
        'Address': '78 High Street, Hampton, UK',
        'Email': 'alanmturing@global.com.uk'
    },
    'Education': {
        'BA & MA': 'University of Cambridge (1931-1934)',
        'PhD': 'Princeton University (1936-1938)'
    },
    'Employment': 'Government Code and Cypher School, Bletchley Park (1939-1942)'
}

marie_cv = {
    'Name':'Marie',
    'Surname':'Skłodowska-Curie',
    'Job Title':'Pyhsicist & Chemist',
    'Contact Information': {
        'Phone': 330156245500,
        'Address': 'Passy, Haute-Savoie, France',
        'Email': 'mariascurie@global.com.fr'
    },
    'Education': {
        'BSc & MSc': 'University of Paris (1891-1893)',
        'PhD': 'University of Paris (1900-1903)'
    },
    'Employment': 'École Normale Supérieure (1897-1906)'
}

stephen_cv = {
    'Name':'Stephen',
    'Surname':'Hawking',
    'Job Title':'Theoretical Physicist',
    'Contact Information': {
        'Phone': 4407702219097,
        'Address': '6 Little St. Mary\'s Lane, Cambridge, UK',
        'Email': 'stephenhawking@global.com.uk'
    },
    'Education': {
        'BA': 'University of Oxford (1959-1962)',
        'PhD': 'University of Cambridge (1962-1966)'
    },
    'Employment': 'University of Cambridge, Applied Mathematics and Theoretical Physics (1962-2009)'
}

sherlock_cv = {
    'Name':'Sherlock',
    'Surname':'Holmes',
    'Job Title':'Consulting Detective',
    'Contact Information': {
        'Phone': 4407700909723,
        'Address': '221B Baker Street, London, UK',
        'Email': 'wsherlocksholmes@global.com.uk'
    },
    'Education': {
        'BSc': 'University of Cambridge (2003-2006)'
    }
}

john_cv = {
    'Name':'John',
    'Surname':'Watson',
    'Job Title':'Doctor',
    'Contact Information': {
        'Phone': 4407700900581,
        'Address': '221B Baker Street, London',
        'Email': 'johnhwatson@global.com.uk'
    },
    'Education': {
        'MBBS': 'St Bartholomew\'s Hospital Medical College (1999-2004)'
    },
    'Employment': 'University College London, General Surgery and Medicine (2004-2006)'
}


cvs = []
cvs = [alan_cv, marie_cv, stephen_cv, sherlock_cv, john_cv]

for i in range(len(cvs)):
    print('CV Number', i+1)
    for key, value in cvs[i].items():
        if type(value) is not dict:    # CV dictionaries contained values that were dicts. So I used an if-else loop to print them prettily.
            print('{key}: {value}'.format(key=key, value=value))
        else:
            print(key)
            for key, value in value.items():
                print('\t {key}: {value}'.format(key=key, value=value)) 
    print('\n')