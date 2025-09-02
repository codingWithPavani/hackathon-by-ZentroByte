from urllib import request
from django.shortcuts import render,redirect
from textblob import TextBlob 
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import get_object_or_404
from .models import Review
from django.db.models import Count
from django.http import JsonResponse
import nltk

# Tell NLTK where to find the vader_lexicon on Render
nltk.data.path.append('/opt/render/project/src/nltk_data')


import sys
sys.path.append('/opt/render/project/src')
import nltk_setup





def index(request):
    return render(request, 'reviews/index.html')


def about(request):
    return render(request, 'reviews/about.html')

def contact(request):
    return render(request, 'reviews/contact.html') 



def home(request):
    # sia = SentimentIntensityAnalyzer()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            
            sia = SentimentIntensityAnalyzer()
            score = sia.polarity_scores(review.review)['compound']
            # review.user = request.user
        

            # Sentiment Analysis
            blob = TextBlob(review.review)
            polarity = blob.sentiment.polarity

            if score > 0.5:
                review.sentiment = "Positive"
            elif score < -0.5:
                review.sentiment = "Negative"
            else:
                review.sentiment = "Neutral"
            
            review.save()  # Save sentiment into DB

            return redirect('home')  # Prevent form resubmission
    else:
        form = ReviewForm()

    # Fetch reviews from DB
    positive_reviews = Review.objects.filter(sentiment="Positive").order_by('-created_at')
    neutral_reviews = Review.objects.filter(sentiment="Neutral").order_by('-created_at')

    return render(request, 'reviews/home.html', {'form': form, 'positive_reviews': positive_reviews, 'neutral_reviews': neutral_reviews})

@login_required(login_url='/login/')
def admin_page(request):
    # Get negative reviews
    negative_reviews = Review.objects.filter(sentiment="Negative").order_by('-created_at')

    context = {
        'negative_reviews': negative_reviews
    }
    return render(request, 'reviews/admin.html', context)

def resolve_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.resolved = True
    review.save()
    return redirect('admin_page')

def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return redirect('admin_page')


 

