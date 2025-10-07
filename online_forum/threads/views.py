from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .services import ThreadService
from .models import Thread

@login_required
def create_thread(request):
    """
    CREATE - Create new thread
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
            return redirect('thread_detail', thread_id=thread.id)
        except Exception as e:
            messages.error(request, f'Error creating thread: {str(e)}')
    
    return render(request, 'threads/create_thread.html')

def thread_list(request):
    """
    READ - List all threads
    """
    threads = ThreadService.get_all_threads()
    return render(request, 'threads/thread_list.html', {'threads': threads})

def thread_detail(request, thread_id):
    """
    READ - Show single thread details
    """
    thread = ThreadService.get_thread_by_id(thread_id)
    if not thread:
        messages.error(request, 'Thread not found.')
        return redirect('thread_list')
    
    return render(request, 'threads/thread_detail.html', {'thread': thread})

@login_required
def update_thread(request, thread_id):
    """
    UPDATE - Edit an existing thread
    """
    thread = ThreadService.get_thread_by_id(thread_id)
    
    if not thread:
        messages.error(request, 'Thread not found.')
        return redirect('thread_list')
    
    # Check if user owns the thread
    if thread.created_by != request.user:
        messages.error(request, 'You can only edit your own threads.')
        return redirect('thread_detail', thread_id=thread_id)
    
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        
        try:
            # Update thread fields
            thread.title = title
            thread.content = content
            thread.save()  # This will trigger validation
            
            messages.success(request, 'Thread updated successfully!')
            return redirect('thread_detail', thread_id=thread.id)
        except Exception as e:
            messages.error(request, f'Error updating thread: {str(e)}')
    
    return render(request, 'threads/update_thread.html', {'thread': thread})

@login_required
def delete_thread(request, thread_id):
    """
    DELETE - Remove a thread
    """
    thread = ThreadService.get_thread_by_id(thread_id)
    
    if not thread:
        messages.error(request, 'Thread not found.')
        return redirect('thread_list')
    
    # Check if user owns the thread
    if thread.created_by != request.user:
        messages.error(request, 'You can only delete your own threads.')
        return redirect('thread_detail', thread_id=thread_id)
    
    if request.method == 'POST':
        try:
            thread_title = thread.title
            thread.delete()
            messages.success(request, f'Thread "{thread_title}" deleted successfully!')
            return redirect('thread_list')
        except Exception as e:
            messages.error(request, f'Error deleting thread: {str(e)}')
    
    return render(request, 'threads/delete_thread.html', {'thread': thread})