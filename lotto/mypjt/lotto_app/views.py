from django.shortcuts import render
from lotto_anal import analyze_lotto_numbers, get_lotto_numbers

def lotto_analysis(request):
    start = 1025  # 시작 회차
    end = 1028  # 종료 회차

    lotto_numbers = get_lotto_numbers(start, end)
    most_common_numbers = analyze_lotto_numbers(lotto_numbers)

    context = {
        'most_common_numbers': most_common_numbers
    }

    return render(request, 'lotto_app/lotto_analysis.html', context)
