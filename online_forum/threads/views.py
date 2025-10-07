from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .services import ThreadService

@login_required
def create_thread(request):
    """
    View for creating new threads using ThreadService
    """
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        
        try:
            # Use service to create thread
            thread = ThreadService.create_thread(
                title=title,
                content=content,
                user=request.user
            )
            messages.success(request, 'Thread created successfully!')
            # Redirect to thread list or detail (we'll implement this later)
            return redirect('thread_list')  
        except Exception as e:
            messages.error(request, f'Error creating thread: {str(e)}')
    
    # If GET request or form has errors, show the creation page
    return render(request, 'threads/create_thread.html')

def thread_list(request):
    """
    View to display all threads using ThreadService
    """
    threads = ThreadService.get_all_threads()
    return render(request, 'threads/thread_list.html', {'threads': threads})

def thread_detail(request, thread_id):
    """
    View to display a single thread using ThreadService
    """
    thread = ThreadService.get_thread_by_id(thread_id)
    if not thread:
        messages.error(request, 'Thread not found.')
        return redirect('thread_list')
    
    return render(request, 'threads/thread_detail.html', {'thread': thread})