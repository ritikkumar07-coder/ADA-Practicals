def naive_string_search(pat, txt):
    M = len(pat)
    N = len(txt)
    found_indices = []

    for i in range(N - M + 1):
        j = 0
        while(j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1
        if (j == M):
            found_indices.append(i)
            
    return found_indices

if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    indices = naive_string_search(pat, txt)
    
    if indices:
        print(f"Pattern '{pat}' found at indices: {indices}")
    else:
        print(f"Pattern '{pat}' not found in text.")
