from django.contrib.auth.models import User
from .models import Thread
from django.core.exceptions import ValidationError

class ThreadService:
    """
    Service layer for thread-related operations
    """
    
    @staticmethod
    def create_thread(title, content, user):
        """
        Service method to create a new thread with validation
        
        Args:
            title (str): Thread title
            content (str): Thread content  
            user (User): Django User object who creates the thread
        
        Returns:
            Thread: The created thread object
        
        Raises:
            ValidationError: If validation fails
            Exception: For other database errors
        """
        try:
            # Create thread instance
            thread = Thread(
                title=title,
                content=content,
                created_by=user
            )
            
            # This will automatically call the clean() method from your model
            # and raise ValidationError if validation fails
            thread.save()
            
            return thread
            
        except ValidationError as e:
            # Re-raise validation errors
            raise e
        except Exception as e:
            # Handle other potential errors
            raise Exception(f"Error creating thread: {str(e)}")
    
    @staticmethod
    def get_thread_by_id(thread_id):
        """
        Get a thread by its ID
        
        Args:
            thread_id (int): Thread ID
        
        Returns:
            Thread: Thread object or None if not found
        """
        try:
            return Thread.objects.get(id=thread_id)
        except Thread.DoesNotExist:
            return None
    
    @staticmethod
    def get_all_threads():
        """
        Get all threads ordered by creation date (newest first)
        
        Returns:
            QuerySet: All thread objects ordered by created_at descending
        """
        return Thread.objects.all()  # Your model Meta.ordering handles the sorting
    
    @staticmethod
    def get_user_threads(user):
        """
        Get all threads created by a specific user
        
        Args:
            user (User): Django User object
        
        Returns:
            QuerySet: Threads created by the user
        """
        return Thread.objects.filter(created_by=user)