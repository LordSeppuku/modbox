Name:    modbox
Version: 1
Release: 1
Summary: modbox

Source0: modbox.sh

License: MIT

Requires(post): info
Requires(preun): info

Requires: podman

BuildArch: noarch

%description
Podman sandbox for GUI applications

%install
mkdir -p %{buildroot}/%{_bindir}
install -p -m 755 %{SOURCE0} %{buildroot}/%{_bindir}

%post
if [ -f "/usr/bin/modbox" ]; then
 unlink /usr/bin/modbox
fi
cp -s /usr/bin/modbox.sh /usr/bin/modbox

%preun
if [ -f "/usr/bin/modbox" ]; then
  unlink /usr/bin/modbox
fi

%files
%{_bindir}/modbox.sh

%changelog
