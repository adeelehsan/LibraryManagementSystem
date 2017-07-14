from django.conf.urls import url, include
from LibraryManagement import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'borrower', views.BorrowerViewSet)
router.register(r'librarian', views.LibrarianViewSet)
router.register(r'borrowbook', views.BookIssueRecordViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^borrowbook/$', views.BookIssueRecordViewSet.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]