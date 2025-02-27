#
# Copyright (C) 2017 by frePPLe bv
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
import os
import pymssql 
from django.db import DEFAULT_DB_ALIAS


def getERPconnection(database=DEFAULT_DB_ALIAS):
    """
    Développement Flowline pour une connexion Sage X3.

    Les paramètres de connexion doivent être définis dans les variables d'environnement.

    Le site https://www.connectionstrings.com/ a un résumé pratique de la syntaxe des chaînes de connexion.

    Pour améliorer la configurabilité du connecteur, nous pouvons utiliser soit :
      a) Des paramètres stockés dans la table de paramètres frePPLe.
         L'avantage est que l'utilisateur final peut alors facilement les modifier.
      b) Des paramètres dans le fichier de paramètres Django de frePPLe.
         Pour stocker les mots de passe et autres informations sensibles, ce fichier est préférable.
    """
    dbname = os.getenv("X3_DBNAME", "default_dbname")
    schema = os.getenv("X3_SCHEMA", "default_schema")
    user = os.getenv("X3_USER", "default_user")
    password = os.getenv("X3_PASSWORD", "default_password")
    host = os.getenv("X3_HOST", "default_host")

    # Split the host and instance if necessary
    if '\\' in host:
        parts = host.split('\\', 1)
        if len(parts) == 2:
            server, instance = parts
            server = f"{server}\\{instance}"
        else:
            raise ValueError("Invalid host format, expected 'server\\instance'")
    else:
        server = host

    return pymssql.connect(server=server, user=user, password=password, database=dbname, timeout=600)
