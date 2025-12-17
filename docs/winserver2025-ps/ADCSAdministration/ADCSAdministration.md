---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 4.0.3.1
Locale: en-US
Module Guid: bcc14c75-ede8-486e-97a5-5bf775c4a221
Module Name: ADCSAdministration
ms.date: 12/27/2016
title: ADCSAdministration
---

# ADCS管理模块
## 描述
这个主题包含了用于管理 Active Directory 证书服务（AD CS）证书颁发机构（CA）角色服务的 Windows PowerShell® cmdlets 的简要描述。表格中的每个 cmdlet 都链接到了有关该 cmdlet 的更多详细信息。

## ADCSAdministrationCmdlets
### [Add-CAAuthorityInformationAccess](./Add-CAAuthorityInformationAccess.md)
为认证机构配置AIA（Automated Infrastructure Authorization）或OCSP（Online Certificate Status Protocol）。

### [Add-CACrlDistributionPoint](./Add-CACrlDistributionPoint.md)
添加一个CRL（证书吊销列表）分发点URI，用于AD CS发布证书吊销信息。

### [Add-CATemplate](./Add-CATemplate.md)
向证书颁发机构（CA）添加一个证书模板。

### [Backup-CARoleService](./Backup-CARoleService.md)
备份CA数据库和私钥信息。

### [Confirm-CAAttestationIdentityKeyInfo](Confirm-CAAttestationIdentityKeyInfo.md)
检查本地证书颁发机构（CA）是否信任用于身份密钥认证的安全硬件。

### [Confirm-CAEndorsementKeyInfo](Confirm-CAEndorsementKeyInfo.md)
检查本地证书颁发机构（CA）是否信任用于密钥认证的安全硬件。

### [Get-CAAuthorityInformationAccess](./Get-CAAuthorityInformationAccess.md)
获取设置在证书颁发机构（CA）属性的“AIA”扩展部分中的AIA和OCSP URI信息。

### [Get-CACrlDistributionPoint](./Get-CACrlDistributionPoint.md)
获取设置在 CA 属性的 CDP 扩展中的所有位置信息。

### [Get-CATemplate](./Get-CATemplate.md)
获取在证书颁发机构（CA）上设置的用于生成证书的模板列表。

### [Remove-CAAuthorityInformationAccess](./Remove-CAAuthorityInformationAccess.md)
从证书颁发机构的AIA扩展集中移除AIA或OCSP URI。

### [Remove-CACrlDistributionPoint](./Remove-CACrlDistributionPoint.md)
从证书颁发机构（CA）中删除CRL分发点（CDP）的URI。

### [Remove-CATemplate](./Remove-CATemplate.md)
从用于证书签发的认证机构（CA）中删除这些模板。

### [ Restore-CARoleService](./Restore-CARoleService.md)
恢复CA数据库和私钥信息。


