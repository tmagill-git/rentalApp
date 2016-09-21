items = ["name","email","num_apps","ssn","move_date","lease_term","dl_info","phone","pets","bankruptcy","felony","eviction","res1addr","res1from","res1to","res1manager","res1phone","res1addr","res2from","res2to","res2manager","res2phone","emp1addr","emp1from","emp1to","emp1manager","emp1phone","emp1income","emp2addr","emp2from","emp2to","emp2manager","emp2phone","emp2income","credit","accounts","ref1addr","ref1length","ref1phone","ref2addr","ref2length"]

for item in items:
    print '    {{ form.' + item + '.label }}'
    print '    {{ form.' + item + ' }}'
    print '      {% for message in form.' + item + '.errors %}'
    print '      <div class="flash">{{ message }}</div>'
    print '      {% endfor %}'
    print ''

