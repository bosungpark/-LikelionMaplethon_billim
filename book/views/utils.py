from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from ..models import MajorBook

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def search(request):
    """
    검색함수
    """
    if request.method == 'POST':
        searched = request.POST['searched']
        books = MajorBook.objects.filter(title__contains=searched)
        paginator = Paginator(books, 8)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        return render(request, 'searched.html', {'searched': searched, 'books': books, 'posts':posts})
    else:
        return render(request, 'searched.html')

def placeholder(request):
    return render(request, 'placeholder.html', {})

def crawler(name):
    """
    '네이버 책'에 연결되어 검색된 책의 이미지 url을 출력하는 크롤러입니다.
    """
    # 크롤링으로 접근하는 웹사이트 주소입니다.(네이버 책에서 name을 검색한 결과 이동된 페이지)
    link='https://book.naver.com/search/search.naver?sm=sta_hty.book&sug=pre&where=nexearch&query='+str(name)
    # webdriver가 설치된 주소를 담은 부분입니다. 만약 빌림을 처음 다운로드 받아 사용하신다면. webdriver를 설치하시고 주소부분을 변경해주셔야 합니다.
    driver = webdriver.Chrome('/Users\HP\Desktop\chromedriver')
    driver.get(link)

    # 네이버 책에서 검색된 결과 리스트 중, 첫 번째 검색결과의 이미지url의 위치입니다.
    book = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchBiblioList"]/li[1]/div/div/a/img')))
    img_link=book.get_attribute("src")

    driver.quit()
    return img_link