-- SQL schema for packages table --
CREATE TABLE IF NOT EXISTS packages (
  distro TEXT,
  distro_version TEXT,
  package TEXT,
  package_version TEXT
);

# Fetching https://deb.debian.org/debian/dists/bookworm/main/binary-amd64/Packages.gz
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'cowsay', '3.03+dfsg2-8');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'curl', '7.88.1-10+deb12u14');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'fzf', '0.38.0-1+b1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'gcc', '4:12.2.0-3');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'git', '1:2.39.5-0+deb12u2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'htop', '3.2.2-2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'jq', '1.6-2.1+deb12u1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'lolcat', '100.0.1-3');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'make', '4.3-4.1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'nano', '7.2-1+deb12u1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'nginx', '1.22.1-9+deb12u3');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'ssh', '1:9.2p1-2+deb12u7');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'libssl-dev', '3.0.17-1~deb12u2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'python3', '3.11.2-1+b1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'rclone', '1.60.1+dfsg-2+b5');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'rsync', '3.2.7-1+deb12u2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'sl', '5.02-1+b1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'tar', '1.34+dfsg-1.2+deb12u1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'tmux', '3.3a-3');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'tree', '2.1.0-1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'unzip', '6.0-28');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'vim', '2:9.0.1378-2+deb12u2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'wget', '1.21.3-1+deb12u1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '12', 'zip', '3.0-13');
# Fetching https://deb.debian.org/debian/dists/bullseye/main/binary-amd64/Packages.gz
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'cowsay', '3.03+dfsg2-8');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'curl', '7.74.0-1.3+deb11u13');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'fzf', '0.24.3-1+b6');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'gcc', '4:10.2.1-1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'git', '1:2.30.2-1+deb11u2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'htop', '3.0.5-7');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'jq', '1.6-2.1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'lolcat', '100.0.1-3');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'make', '4.3-4.1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'nano', '5.4-2+deb11u3');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'nginx', '1.18.0-6.1+deb11u3');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'ssh', '1:8.4p1-5+deb11u3');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'libssl-dev', '1.1.1w-0+deb11u1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'python3', '3.9.2-3');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'rclone', '1.53.3-1+b6');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'rsync', '3.2.3-4+deb11u1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'sl', '5.02-1+b1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'tar', '1.34+dfsg-1+deb11u1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'tmux', '3.1c-1+deb11u1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'tree', '1.8.0-1+b1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'unzip', '6.0-26+deb11u1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'vim', '2:8.2.2434-3+deb11u1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'wget', '1.21-1+deb11u1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '11', 'zip', '3.0-12');
# Fetching https://deb.debian.org/debian/dists/trixie/main/binary-amd64/Packages.gz
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'cowsay', '3.03+dfsg2-8');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'curl', '8.14.1-2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'fzf', '0.60.3-1+b2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'gcc', '4:14.2.0-1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'git', '1:2.47.3-0+deb13u1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'htop', '3.4.1-5');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'jq', '1.7.1-6+deb13u1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'lolcat', '100.0.1-4');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'make', '4.4.1-2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'nano', '8.4-1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'nginx', '1.26.3-3+deb13u1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'ssh', '1:10.0p1-7');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'libssl-dev', '3.5.1-1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'python3', '3.13.5-1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'rclone', '1.60.1+dfsg-4');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'rsync', '3.4.1+ds1-5');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'sl', '5.02-1+b1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'tar', '1.35+dfsg-3.1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'tmux', '3.5a-3');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'tree', '2.2.1-1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'unzip', '6.0-29');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'vim', '2:9.1.1230-2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'wget', '1.25.0-2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('debian', '13', 'zip', '3.0-15');
# Fetching https://archive.ubuntu.com/ubuntu/dists/focal/main/binary-amd64/Packages.gz
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '20.04', 'curl', '7.68.0-1ubuntu2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '20.04', 'gcc', '4:9.3.0-1ubuntu2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '20.04', 'git', '1:2.25.1-1ubuntu3');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '20.04', 'htop', '2.2.0-2build1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '20.04', 'libssl-dev', '1.1.1f-1ubuntu2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '20.04', 'make', '4.2.1-1.2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '20.04', 'nano', '4.8-1ubuntu1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '20.04', 'nginx', '1.17.10-0ubuntu1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '20.04', 'python3', '3.8.2-0ubuntu2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '20.04', 'rsync', '3.1.3-8');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '20.04', 'ssh', '1:8.2p1-4');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '20.04', 'tar', '1.30+dfsg-7');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '20.04', 'tmux', '3.0a-2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '20.04', 'unzip', '6.0-25ubuntu1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '20.04', 'vim', '2:8.1.2269-1ubuntu5');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '20.04', 'wget', '1.20.3-1ubuntu1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '20.04', 'zip', '3.0-11build1');
# Fetching https://archive.ubuntu.com/ubuntu/dists/jammy/main/binary-amd64/Packages.gz
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'curl', '7.81.0-1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'gcc', '4:11.2.0-1ubuntu1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'git', '1:2.34.1-1ubuntu1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'htop', '3.0.5-7build2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'jq', '1.6-2.1ubuntu3');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'libssl-dev', '3.0.2-0ubuntu1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'make', '4.3-4.1build1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'nano', '6.2-1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'nginx', '1.18.0-6ubuntu14');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'python3', '3.10.4-0ubuntu2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'rsync', '3.2.3-8ubuntu3');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'ssh', '1:8.9p1-3');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'tar', '1.34+dfsg-1build3');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'tmux', '3.2a-4build1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'unzip', '6.0-26ubuntu3');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'vim', '2:8.2.3995-1ubuntu2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'wget', '1.21.2-2ubuntu1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '22.04', 'zip', '3.0-12build2');
# Fetching https://archive.ubuntu.com/ubuntu/dists/noble/main/binary-amd64/Packages.gz
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'curl', '8.5.0-2ubuntu10');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'gcc', '4:13.2.0-7ubuntu1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'git', '1:2.43.0-1ubuntu7');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'htop', '3.3.0-4build1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'jq', '1.7.1-3build1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'libssl-dev', '3.0.13-0ubuntu3');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'make', '4.3-4.1build2');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'nano', '7.2-2build1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'nginx', '1.24.0-2ubuntu7');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'python3', '3.12.3-0ubuntu1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'rsync', '3.2.7-1ubuntu1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'ssh', '1:9.6p1-3ubuntu13');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'tar', '1.35+dfsg-3build1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'tmux', '3.4-1build1');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'unzip', '6.0-28ubuntu4');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'vim', '2:9.1.0016-1ubuntu7');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'wget', '1.21.4-1ubuntu4');
INSERT INTO packages (distro, distro_version, package, package_version) VALUES ('ubuntu', '24.04', 'zip', '3.0-13build1');
