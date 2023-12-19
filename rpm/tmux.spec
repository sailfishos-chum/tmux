# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       tmux

# >> macros
# << macros
%define bcversion 1.0.0

Summary:    A Terminal Multiplexer
Version:    3.3a
Release:    0
Group:      Applications
License:    ISC
URL:        https://github.com/tmux/tmux
Source0:    %{name}-%{version}.tar.gz
Source100:  tmux.yaml
Source101:  tmux-rpmlintrc
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(tinfo)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  bison
BuildRequires:  libutempter-devel

%description
%{summary}.

It enables a number of terminals to be created, accessed, and controlled
from a single screen. tmux may be detached from a screen and continue
running in the background, then later reattached.

%if "%{?vendor}" == "chum"
Title: tmux
Type: console-application
PackagedBy: nephros
Categories:
  - TerminalEmulator
  - Utility
Custom:
  Repo: %{url}
  PackagingRepo: https://github.com/sailfishos-chum/tmux
PackageIcon: https://raw.githubusercontent.com/tmux/tmux/master/logo/tmux-logomark.svg
Links:
  Homepage: %{url}
  Help: %{url}/discussions
  Bugtracker: %{url}/issues
  Donation: https://openrepos.net/donate
%endif


%package bash-completion
Summary:    Shell completions for %{name}
License:    GPLv2
Group:      Applications
Requires:   gnu-bash

%description bash-completion
%if "%{?vendor}" == "chum"
Title: Shell completions for %{name}
Type: addon
PackagedBy: nephros
Categories:
  - Files
Custom:
  Repo: %{url}
  PackagingRepo: https://github.com/sailfishos-chum/tmux
PackageIcon: https://raw.githubusercontent.com/tmux/tmux/master/logo/tmux-logomark.svg
Links:
  Homepage: %{url}
  Help: %{url}/discussions
  Bugtracker: %{url}/issues
  Donation: https://openrepos.net/donate
%endif


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
# << build pre

%autogen --disable-static
%configure --disable-static \
    --enable-systemd \
    --enable-utempter

make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
pushd %{builddir}/tmux-bash-completion/
install -d %{buildroot}%{_datadir}/bash-completion/completions/
install -m644 completions/tmux %{buildroot}%{_datadir}/bash-completion/completions/
rm -rf %{buildroot}%{_docdir}
rm -rf %{buildroot}%{_mandir}
# << install post

%files
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/*
# >> files
# << files

%files bash-completion
%defattr(-,root,root,-)
%{_datadir}/bash-completion/completions/%{name}
# >> files bash-completion
# << files bash-completion
