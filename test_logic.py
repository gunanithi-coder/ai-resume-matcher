from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def run_test():
    test_cases = [
        {"r": "Python Developer", "j": "Python Developer", "expected": "High"},
        {"r": "Java Specialist", "j": "Python Developer", "expected": "Low"},
    ]
    
    v = TfidfVectorizer()
    for case in test_cases:
        matrix = v.fit_transform([case['r'], case['j']])
        score = cosine_similarity(matrix[0:1], matrix[1:2])[0][0]
        print(f"Resume: {case['r']} | JD: {case['j']}")
        print(f"Score: {score:.2f} | Expected: {case['expected']}\n")

if __name__ == "__main__":
    run_test()