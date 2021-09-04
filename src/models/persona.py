from config.db import cadenaConexion
def listadoPersona():
    try:
        db = cadenaConexion()
        cur = db.cursor()
        sql ="SELECT * FROM datos"
        cur.execute(sql)
        return cur.fetchall()
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()

def listadoPersonaID(id):
    try:
        db = cadenaConexion()
        cur = db.cursor()
        sql ="SELECT * FROM datos WHERE id = ?"
        cur.execute(sql,[id])
        return cur.fetchone()
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()

def guardarPersona(dni,nombres,fecha,correo):
    try:
        db = cadenaConexion()
        cur = db.cursor()
        sql ="INSERT INTO datos (dni,nombres,fechaNacimiento,correo) VALUES (?,?,?,?)"
        cur.execute(sql,[dni,nombres,fecha,correo])
        return db.commit()
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()


def actualizarPersona(dni,nombres,fecha,correo,id):
    try:
        db = cadenaConexion()
        cur = db.cursor()
        sql ="UPDATE datos SET dni= ?, nombres = ?, fechaNacimiento = ?, correo = ? WHERE id = ?"
        cur.execute(sql,[dni,nombres,fecha,correo,id])
        return db.commit()
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()


def eliminarPersona(id):
    try:
        db = cadenaConexion()
        cur = db.cursor()
        sql ="DELETE FROM datos WHERE id = ?"
        cur.execute(sql,[id])
        return db.commit()
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()

def validarDni1(dni):
    try:
        db = cadenaConexion()
        cur = db.cursor()
        sql ="SELECT * FROM datos WHERE dni = ?"
        cur.execute(sql,[dni])
        return cur.fetchone()
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()

def validarDni2(dni,id):
    try:
        db = cadenaConexion()
        cur = db.cursor()
        sql ="SELECT COUNT(*) FROM datos WHERE dni=? OR id=?"
        cur.execute(sql,[dni,id])
        return cur.fetchone()[0]
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()

def validarCorreo1(correo):
    try:
        db = cadenaConexion()
        cur = db.cursor()
        sql ="SELECT * FROM datos WHERE correo = ?"
        cur.execute(sql,[correo])
        return cur.fetchone()
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()

def validarCorreo2(correo,id):
    try:
        db = cadenaConexion()
        cur = db.cursor()
        sql ="SELECT COUNT(*) FROM datos WHERE correo=? OR id=?"
        cur.execute(sql,[correo,id])
        return cur.fetchone()[0]
    except Exception as e:
        return e
    finally:
        cur.close()
        db.close()