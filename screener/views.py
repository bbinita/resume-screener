from django.shortcuts import render, redirect
from .utils import extract_text_from_pdf, analyze_resume

def index(request):
    return render(request, 'screener/index.html')

def result(request):
    if request.method == "POST":

        if 'resume' not in request.FILES:
            return render(request, 'screener/index.html', {
                'error': 'Please upload a resume file.'
            })

        resume_file = request.FILES['resume']

        if not resume_file.name.endswith('.pdf'):
            return render(request, 'screener/index.html', {
                'error': 'Only PDF files are allowed.'
            })

        job_description = request.POST.get('job_description', '').strip()
        if not job_description:
            return render(request, 'screener/index.html', {
                'error': 'Job description cannot be empty.'
            })

        resume_text = extract_text_from_pdf(resume_file)

        if not resume_text:
            return render(request, 'screener/index.html', {
                'error': 'Could not extract text from PDF. Try another file.'
            })

        results = analyze_resume(resume_text, job_description)

        return render(request, 'screener/result.html', {'results': results})

    else:
        return redirect('index')