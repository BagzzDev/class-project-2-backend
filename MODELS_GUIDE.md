# Adding a New Model — Quick Guide

> Django auto-creates the `id` field. Don't add it yourself.

---

## 1. `movies/models.py` — Add the class

```python
class SocialLink(models.Model):
    name         = models.CharField(max_length=50)
    anchor_class = models.CharField(max_length=2)
    icon_class   = models.CharField(max_length=30)
    url          = models.CharField(max_length=200)

    def __str__(self):
        return self.name
```

**Field type cheat sheet:**
| ER Diagram type | Django field |
|---|---|
| varchar(n) | `models.CharField(max_length=n)` |
| int | `models.IntegerField()` |
| string | `models.TextField()` |

---

## 2. `movies/admin.py` — Register it

```python
from .models import SocialLink

admin.site.register(SocialLink)
```

---

## 3. Terminal — Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

Do this every time you add or change a model. Verify the table appeared in pgAdmin.

---

## 4. `movies/views.py` — Query and pass to template

```python
from .models import SocialLink

def index(request):
    context = {
        'social_links': SocialLink.objects.all(),
    }
    return render(request, 'index.html', context)
```

---

## 5. Template — Replace hardcoded HTML with a loop

```html
{% for link in social_links %}
    <a href="{{ link.url }}">{{ link.name }}</a>
{% endfor %}
```

---

## 6. Admin panel — Add your data

1. Go to `http://127.0.0.1:8000/admin/`
2. Find your model and click **Add**
3. Fill in the fields and save
4. Refresh the homepage — data should appear

---

## When do I need to re-run things?

| Change made | Action needed |
|---|---|
| Added/edited a model field | `makemigrations` + `migrate` |
| Edited views.py or a template | Nothing — Django auto-reloads |
| Added data in admin | Just refresh the page |
