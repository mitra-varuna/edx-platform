from django.conf.urls import include, patterns, url
from django.views.generic import TemplateView

from verify_student import views

urlpatterns = patterns(
    '',
    url(
        r'^show_requirements/(?P<course_id>[^/]+/[^/]+/[^/]+)$',
        views.show_requirements,
        name="verify_student_show_requirements"
    ),

    url(
        r'^verify/(?P<course_id>[^/]+/[^/]+/[^/]+)$',
        views.VerifyView.as_view(),
        name="verify_student_verify"
    ),

    url(
        r'^verified/(?P<course_id>[^/]+/[^/]+/[^/]+)$',
        views.VerifiedView.as_view(),
        name="verify_student_verified"
    ),

    url(
        r'^create_order',
        views.create_order,
        name="verify_student_create_order"
    ),

    url(
        r'^results_callback$',
        views.results_callback,
        name="verify_student_results_callback",
    ),

    url(
        r'^reverify$',
        views.ReverifyView.as_view(),
        name="verify_student_reverify"
    ),

    url(
        r'^midcourse_reverify$',
        views.MidCourseReverifyView.as_view(),
        name="verify_student_midcourse_reverify"
    ),

    url(
        r'^reverification_confirmation$',
        views.reverification_submission_confirmation,
        name="verify_student_reverification_confirmation"
    ),

    url(
        r'^midcourse_reverification_confirmation$',
        views.midcourse_reverification_confirmation,
        name="verify_student_midcourse_reverification_confirmation"
    ),

    url(
        r'^midcourse_reverify_dash$',
        views.midcourse_reverify_dash,
        name="verify_student_midcourse_reverify_dash"
    ),
)
