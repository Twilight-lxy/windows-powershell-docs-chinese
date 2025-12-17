---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
Download Help Link: https://aka.ms/winsvr-2025-pshelp
Help Version: 5.0.1.1
Locale: en-US
Module Guid: beb3db13-eed6-4f7b-8420-079e395b58f9
Module Name: ADRMSADMIN
ms.date: 12/20/2016
title: ADRMSADMIN
---

# ADRMSADMIN 模块
## 描述
这个主题简要介绍了用于在 Windows Server 中管理 Active Directory 权限管理服务（AD RMS）的 Windows PowerShell cmdlet。表格中的每个 cmdlet 都链接到了有关该 cmdlet 的更多信息。这些 cmdlet 使您能够使用 PowerShell 来管理 AD RMS 集群。

## ADRMSADMINCmdlets
### [Export-RmsReportDefinitionLanguage](./Export-RmsReportDefinitionLanguage.md)
导出所有报告定义文件（.rdl格式）。

### [Export-RmsTPD](./Export-RmsTPD.md)
将TPD导出到AD RMS中。

### [Export-RmsTUD](./Export-RmsTUD.md)
导出一个TUD文件。

### [Get-RmsCertChain](./Get-RmsCertChain.md)
生成一份关于特定用户请求的证书链的报告，该报告针对的是AD RMS集群。

### [Get-RmsCertInfo](./Get-RmsCertInfo.md)
生成一份关于在用户请求中使用的证书的报告，该证书用于AD RMS集群。

### [Get-RmsChildCert](./Get-RmsChildCert.md)
从用于用户请求的父证书中返回所有子证书（这些父证书是AD RMS集群的一部分）。

### [Get-RmsEncryptedIL](./Get-RmsEncryptedIL.md)
从用户请求中使用的发行许可证中返回与 Active Directory 权限管理服务（AD RMS）集群相关的使用许可信息。

### [Get-RmsRequestInfo](./Get-RmsRequestInfo.md)
为AD RMS集群中的特定用户请求生成一份报告。

### [Get-RmsSvcAccount](./Get-RmsSvcAccount.md)
获取用于 Active Directory 权限管理服务（AD RMS）集群的服务账户凭据。

### [Get-RmsSystemHealthReport](./Get-RmsSystemHealthReport.md)
生成Active Directory Rights Management Services（AD RMS）集群的系统健康报告。

### [Get-RmsUserRequestReport](./Get-RmsUserRequestReport.md)
生成 AD RMS 集群的用户请求统计报告。

### [Import-RmsTPD](./Import-RmsTPD.md)
从 AD RMS 中的文件导入一个 TPD（传输保护数据）。

### [Import-RmsTUD](./Import-RmsTUD.md)
从 AD RMS 文件中导入 TUD（信任声明），或指定要信任的 Microsoft 账户 ID。

### [Initialize-RmsCryptoMode2](./Initialize-RmsCryptoMode2.md)
为AD RMS服务器过渡到加密模式2做好准备。

### [Install-RmsMfgEnrollment](./Install-RmsMfgEnrollment.md)
将一台 AD RMS 服务器注册到 Microsoft Federation Gateway 中。

### [Install-RmsMfgSupport](./Install-RmsMfgSupport.md)
为AD RMS服务器添加对Microsoft Federation Gateway的支持。

### [Set-RmsSvcAccount](./Set-RmsSvcAccount.md)
为AD RMS集群设置服务账户。

### [Uninstall-RmsMfgEnrollment](./Uninstall-RmsMfgEnrollment.md)
终止将 AD RMS 服务器与 Microsoft Federation Gateway 配置为联盟环境的操作。

### [卸载RmsMfgSupport](./Uninstall-RmsMfgSupport.md)
从AD RMS服务器中移除对Microsoft Federation Gateway的支持。

### [Update-RmsCluster](./Update-RmsCluster.md)
更新AD RMS集群的信息。

### [更新RMS制造商注册信息](./Update-RmsMfgEnrollment.md)
更新已注册到 Microsoft Federation Gateway 服务的 AD RMS 服务器的注册信息。


