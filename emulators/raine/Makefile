# $NetBSD: Makefile,v 1.35 2020/08/31 18:09:28 wiz Exp $
#

DISTNAME=	raines-0.43.3
PKGNAME=	${DISTNAME:S/raines/raine/}
PKGREVISION=	13
CATEGORIES=	emulators
MASTER_SITES=	http://rainemu.swishparty.co.uk/html/archive/
EXTRACT_SUFX=	.tar.bz2

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	http://rainemu.swishparty.co.uk/
COMMENT=	680x0 Arcade Emulator

BUILD_DEPENDS+=	nasm-[0-9]*:../../devel/nasm

WRKSRC=		${WRKDIR}/${PKGNAME_NOREV}
USE_TOOLS+=	gmake perl:run pkg-config
MAKE_FILE=	makefile
MAKE_ENV+=	OSTYPE=linux
REPLACE_PERL=	makedep
PTHREAD_OPTS+=	require

INSTALL_MAKE_FLAGS+=	prefix=${DESTDIR}${PREFIX}

# Uses i386 assembler.
ONLY_FOR_PLATFORM=	*-*-i386

post-build:
	(${ECHO} "#!${SH}";					\
	 ${ECHO} "cd ${PREFIX}/share/raine && ./raine $$@")	\
		> ${WRKSRC}/raine.sh

post-install:
	${MV} ${DESTDIR}${PREFIX}/bin/raine ${DESTDIR}${PREFIX}/share/raine
	${INSTALL_SCRIPT} ${WRKSRC}/raine.sh ${DESTDIR}${PREFIX}/bin/raine

.include "../../devel/SDL/buildlink3.mk"
.include "../../devel/allegro/buildlink3.mk"
.include "../../devel/zlib/buildlink3.mk"
.include "../../graphics/png/buildlink3.mk"
.include "../../sysutils/desktop-file-utils/desktopdb.mk"
.include "../../mk/pthread.buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
