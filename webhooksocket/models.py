from django.db import models
from django.urls import reverse
import secrets


def random_ident():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return "".join(secrets.choice(characters) for i in range(64))


class Bridge(models.Model):
    name = models.CharField(max_length=60)
    hook_ident = models.CharField(
        verbose_name="Webhook Unique Identifier",
        max_length=64, unique=True,
        db_index=True, default=random_ident
    )
    socket_ident = models.CharField(
        verbose_name="Websocket Unique Identifier",
        max_length=64, unique=True,
        db_index=True, default=random_ident
    )
    description = models.CharField(max_length=1024, default="", blank=True)

    def hook_url(self):
        return reverse('webhooksocket:hooks', kwargs={
            "ident": self.hook_ident
        })

    def socket_url(self):
        return reverse('webhooksocket:sockets', kwargs={
            "ident": self.socket_ident
        })
