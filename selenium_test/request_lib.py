# encoding: utf-8
import urllib2




def request_txt(site):
    hdr = {'Host':'pan.baidu.com','User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36','cookie':'BAIDUID=50D69C72F98A07624EC5DA75711F2E0B:FG=1; BIDUPSID=50D69C72F98A07624EC5DA75711F2E0B; PSTM=1459843710; PANWEB=1; bdshare_firstime=1459921997754; BDUSS=mE4My05LU9RYkdFbzJxRkx5ZjBkRmNwQ0JkcmFNa1FhbTl-Q2d4S29WRm9OMUJYQVFBQUFBJCQAAAAAAAAAAAEAAAApejtW1eLKx8uttcTLrTEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGiqKFdoqihXU; secu=1; MCITY=-%3A; BDSFRCVID=7m0sJeC62xSChP3RFl-WbcJdRHM_DJoTH6aIKaFW8_PNquCEajsuEG0Ptf8g0Ku-8_AoogKKKgOTHI6P; H_BDCLCKID_SF=fnID_K-Kf-3bfTrg-tcHMDCShGRq-pOeWDTm_DoyLhOsVKO-Q4vdL4DSyxONBUrd3gQy-pPKKlTvHqQ5ehnmXR_0LPoKaJJt3mkjbPbDfn02OPKzehnNhP4syPRiKMRnWgKqbIFyJCDbMKLr5nJbq40_hfQ0etJXfbvLoPOF5l8-h4nbLP7mDpDzh2cU5tJZ5Nr72x7gWJ7xOKQpyfRHQlbbBn3wbRQm3C6BQ-5N3KJmfbL9bT3v5DrbBPQy2-biW23M2MbdWCQmbRO4-TFMD6bbefK; H_WISE_SIDS=102065_100273_100288_107851_100099_109607_104341_106323_106186_108437_108780_109921_109700_109794_108411_107960_108454_109737_109890_109558_109531_107896_107917_109683_109498_107806_109587_108342_108295_109985_107311_107242_100460; STOKEN=5f781b7212b57c63f3298d9634d7466bfac91b7e61db68e5f4e4c26f887c9f01; SCRC=356d5eaf427ab31e76a3e7558fe3ddb6; BAIDU_SSP_lcr=https://www.google.com.au/; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=1432_19037_18241_17947_21118_21160_20929; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1473829166,1473836628; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1474163451; PANPSC=13798835240233783331%3AENVL4Mn25ShKeos2hhgdg%2Bn90oj%2BY%2FIs34lshz6CkL%2BRhxLNg7Jg8452N20FG1l54huX1R9Xo1kwwo4y0uRbvSy6%2B%2BBAeydjmInu55rmWmL%2F5yY%2B2yl0OZpZfis7W4JlvY40bMUDX1j76jyG3uDkPYshZ7OchQK1KQDQpg%2B6XCV%2BSJWX9%2F9F%2FIkt7vMgzc%2BT; cflag=15%3A3'}
    req = urllib2.Request(site, headers=hdr)
    page = urllib2.urlopen(req)
    print page.read()
#     print page.get_cookie()

# request_txt('https://pan.baidu.com/disk/home#list/path=%2F')


