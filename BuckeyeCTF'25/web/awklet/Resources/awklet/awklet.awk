#!/bin/awk -f
BEGIN {
    SUBSEP = "@"
    HEIGHT = 7

    printf("Status: 200 OK\n")
    printf("Content-type: text/plain\n\n")

    parse_query(ENVIRON["QUERY_STRING"], GET)

    for (i = 32; i <= 255; i++) {
        ord[sprintf("%c", i)] = i
    }

    if ("name" in GET) {
        font_name = (("font" in GET) ? GET["font"] : "standard")
        text = GET["name"]
        render_ascii(text, font_name)
    }
}

function urldecode(str,    i, hex, out, c) {
    out = ""
    i = 1

    while (i <= length(str)) {
        c = substr(str, i, 1)

        if (c == "+") out = out " "
        else if (c == "%") {
            hex = substr(str, i + 1, 2)
            out = out sprintf("%c", strtonum("0x" hex))
            i += 2
        }
        else out = out c

        i++
    }

    return out
}

function parse_query(qs, GET,    start, key, val, pair) {
    start = 1

    while (match(substr(qs, start), /([^&=]+)=?([^&]*)/, pair)) {
        key = urldecode(pair[1])
        val = urldecode(pair[2])
        GET[key] = val
        start += RSTART + RLENGTH - 1
    }
}

function load_font(font_name, font,    filename, line, char, row, c) {
    filename = font_name ".txt"
    char = 32
    row = 0

    while ((getline line < filename) > 0) {
        font[char, row] = line
        row++

        if (row == HEIGHT) {
            char++
            row = 0
        }
    }

    close(filename)
}

function render_ascii(text, font_name,    font, i, j, c, char, line_out) {
    load_font(font_name, font)

    print "Here's your " font_name " ascii art:\n"

    for (i = 0; i < HEIGHT; i++) {
        line_out = ""

        for (j = 1; j <= length(text); j++) {
            c = substr(text, j, 1)
            char = ord[c]
            line_out = line_out font[char, i] " "
        }

        print line_out
    }
}
