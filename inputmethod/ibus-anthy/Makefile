# $NetBSD: Makefile,v 1.24 2020/12/04 20:45:24 nia Exp $

DISTNAME=	ibus-anthy-1.5.12
CATEGORIES=	inputmethod japanese
MASTER_SITES=	https://github.com/ibus/ibus-anthy/releases/download/${PKGVERSION_NOREV}/

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/ibus/ibus/wiki
COMMENT=	Anthy engine for IBus input platform
LICENSE=	gnu-gpl-v2

DEPENDS+=	kasumi>=2.1:../../inputmethod/kasumi
DEPENDS+=	ibus>=1.5.4:../../inputmethod/ibus
DEPENDS+=	${PYPKGPREFIX}-gobject3-[0-9]*:../../devel/py-gobject3

GNU_CONFIGURE=		yes
USE_LIBTOOL=		yes
USE_PKGLOCALEDIR=	yes
USE_LANGUAGES=		c
USE_TOOLS+=		pkg-config msgfmt gmake

GETTEXT_TOOLS_REQD=	0.19.7

CONFIGURE_ARGS+=	--localedir=${PREFIX}/${PKGLOCALEDIR}/locale
CONFIGURE_ARGS+=	--with-kasumi-exec=${LOCALBASE}/bin/kasumi
CONFIGURE_ARGS+=	--with-kasumi-icon=${LOCALBASE}/share/pixmaps/kasumi.png
CONFIGURE_ARGS+=	--with-layout=default
#CONFIGURE_ARGS+=	--enable-pygtk2-anthy

.include "../../devel/gettext-lib/buildlink3.mk"
BUILDLINK_API_DEPENDS.glib2+=		glib2>=2.26.0
.include "../../devel/glib2/buildlink3.mk"
BUILDLINK_DEPMETHOD.gobject-introspection=	build
.include "../../devel/gobject-introspection/buildlink3.mk"
.include "../../lang/python/application.mk"
.include "../../inputmethod/anthy/buildlink3.mk"
.include "../../devel/glib2/schemas.mk"
.include "../../mk/bsd.pkg.mk"
