# $NetBSD: Makefile,v 1.10 2020/11/29 21:58:03 dbj Exp $

DISTNAME=	ddrescue-1.25
CATEGORIES=	sysutils
MASTER_SITES=	${MASTER_SITE_GNU:=ddrescue/}
EXTRACT_SUFX=	.tar.lz

MAINTAINER=	ef@math.uni-bonn.de
HOMEPAGE=	https://www.gnu.org/software/ddrescue/ddrescue.html
COMMENT=	GNU ddrescue is a data recovery tool
LICENSE=	gnu-gpl-v2

HAS_CONFIGURE=		YES
USE_LANGUAGES=		c++
USE_TOOLS+=		gmake
INFO_FILES=		YES

CONFIGURE_ARGS+=	CC=${CC:Q} CXX=${CXX:Q} CPPFLAGS=${CPPFLAGS:Q}
CONFIGURE_ARGS+=	CFLAGS=${CFLAGS:Q} CXXFLAGS=${CXXFLAGS:Q}
CONFIGURE_ARGS+=	LDFLAGS=${LDFLAGS:Q}
CONFIGURE_ARGS+=	--prefix=${PREFIX}
CONFIGURE_ARGS+=	--infodir=${PREFIX}/${PKGINFODIR}
CONFIGURE_ARGS+=	--mandir=${PREFIX}/${PKGMANDIR}
CONFIGURE_ARGS+=	--sysconfdir=${PKG_SYSCONFDIR}

TEST_TARGET=		check
INSTALL_TARGET=		install install-man

.include "../../mk/bsd.pkg.mk"
