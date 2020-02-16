class markCacophony:

    
    def markVowelHiatus (text):
        reVowelHiatus = re.compile('(?i)[αὰάἁἀἂἃἅἄᾳᾂᾃἆἇᾷᾆᾇᾶεὲέἐἑἒἓἕἔιὶίἰἱἲἳἵἴἶἷῖϊοὸόὀὁὂὃὄὅυὺύὑὐὒὓὔὕὖὗϋωὼώὠὡὢὣὤὥὦὧῶῲῴῷῳᾧᾦᾢᾣᾡᾠηὴήἠἡἢἣἥἤἧἦῆῄῂῇῃᾓᾒᾗᾖᾑᾐ]\s+[αὰάἁἀἂἃἅἄᾳᾂᾃἆἇᾷᾆᾇᾶεὲέἐἑἒἓἕἔιὶίἰἱἲἳἵἴἶἷῖϊοὸόὀὁὂὃὄὅυὺύὑὐὒὓὔὕὖὗϋωὼώὠὡὢὣὤὥὦὧῶῲῴῷῳᾧᾦᾢᾣᾡᾠηὴήἠἡἢἣἥἤἧἦῆῄῂῇῃᾓᾒᾗᾖᾑᾐ]')
        underlineFormat = '\033[{0}m'
        colorFormat = '\033[{0}m'
        underlineStr = underlineFormat.format(4)
        colorStr = colorFormat.format(43)
        resetStr = colorFormat.format(0)

        lastMatch = 0
        formattedText = ''
        for match in re.finditer(reVowelHiatus, text):
            start, end = match.span()
            formattedText += text[lastMatch: start]
            formattedText += colorStr
            formattedText += underlineStr
            formattedText += text[start: end]
            formattedText += resetStr
            lastMatch = end

        formattedText += text[lastMatch:]

        print (formattedText)
        

    def markNasalConsonant(text):
        reNasalConsonant = re.compile('(?i)[μν]\s+[βγδκπτθφχ]')
        underlineFormat = '\033[{0}m'
        colorFormat = '\033[{0}m'
        underlineStr = underlineFormat.format(4)
        colorStr = colorFormat.format(43)
        resetStr = colorFormat.format(0)

        lastMatch = 0
        formattedText = ''
        for match in re.finditer(reNasalConsonant, text):
            start, end = match.span()
            formattedText += text[lastMatch: start]
            formattedText += colorStr
            formattedText += underlineStr
            formattedText += text[start: end]
            formattedText += resetStr
            lastMatch = end

        formattedText += text[lastMatch:]

        print (formattedText)

    def markConsonantHiatus(text):
        reConsonantHiatus = re.compile('(?i)[ςρῥτθπσδφγξκλχβνμξζψ]\s+[ςρῥτθπσδφγξκλχβνμξζψ]')
        underlineFormat = '\033[{0}m'
        colorFormat = '\033[{0}m'
        underlineStr = underlineFormat.format(4)
        colorStr = colorFormat.format(43)
        resetStr = colorFormat.format(0)

        lastMatch = 0
        formattedText = ''
        for match in re.finditer(reConsonantHiatus, text):
            start, end = match.span()
            formattedText += text[lastMatch: start]
            formattedText += colorStr
            formattedText += underlineStr
            formattedText += text[start: end]
            formattedText += resetStr
            lastMatch = end

        formattedText += text[lastMatch:]

        print (formattedText)

    def markNonGreekOnset(text):
        reNonGreekOnset = re.compile('(?i)\s(κ[θδμ]|χ[τδμ]|γ[τθμ]|σ[δγνλρβ]|πμ|φ[μν]|β[μν]|τ[νπκ]|θ[μφχ]|δ[βγ]|μ[μρτθπσδφγξκλχβξζψ])')
        underlineFormat = '\033[{0}m'
        colorFormat = '\033[{0}m'
        underlineStr = underlineFormat.format(4)
        colorStr = colorFormat.format(43)
        resetStr = colorFormat.format(0)

        lastMatch = 0
        formattedText = ''
        for match in re.finditer(reNonGreekOnset, text):
            start, end = match.span()
            formattedText += text[lastMatch: start]
            formattedText += colorStr
            formattedText += underlineStr
            formattedText += text[start: end]
            formattedText += resetStr
            lastMatch = end

        formattedText += text[lastMatch:]

        print (formattedText)

    def markNonGreekCoda(text):
        reNonGreekCoda = re.compile('(?i)([^νραειουηω]|[ςτθπσδφξκλχβμζψ]ξ|[ςρτθπσδφγξκλχβνξζψ]ψ|[ςρτθπσδφγξκχβνμζψ]ς|[ςρτθπσδφγξκλχβνμζψ]σ)(?=\s)')
        underlineFormat = '\033[{0}m'
        colorFormat = '\033[{0}m'
        underlineStr = underlineFormat.format(4)
        colorStr = colorFormat.format(43)
        resetStr = colorFormat.format(0)

        lastMatch = 0
        formattedText = ''
        for match in re.finditer(reNonGreekCoda, text):
            start, end = match.span()
            formattedText += text[lastMatch: start]
            formattedText += colorStr
            formattedText += underlineStr
            formattedText += text[start: end]
            formattedText += resetStr
            lastMatch = end

        formattedText += text[lastMatch:]

        print (formattedText)
