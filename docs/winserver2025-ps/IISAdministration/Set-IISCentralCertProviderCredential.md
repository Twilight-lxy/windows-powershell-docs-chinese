---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/set-iiscentralcertprovidercredential?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IISCentralCertProviderCredential
---

# 设置 IISCentralCertProvider 的凭据

## 摘要
修改用于 IIS 证书存储的用户账户凭据。

## 语法

```
Set-IISCentralCertProviderCredential [-UserName] <String> [<CommonParameters>]
```

## 描述
`Set-IISCentralCertProviderCredential` cmdlet 允许您更改用于访问 IIS 中心证书存储的用户账户。中心证书存储可以将所有的 IIS 证书保存在一个集中式的位置（例如文件共享资源）；IIS 服务器会从该集中式位置获取证书。这意味着您只需在其中一个位置安装证书，而无需在每一台 IIS 服务器上都单独安装相同的证书。

服务器通过使用预先配置的用户账户来访问中央证书存储库。该用户账户可以是本地账户，也可以是域账户，但必须具有对该证书存储库位置的只读访问权限。在首次启用证书存储库时，您需要指定一个用户账户。不过，您可以通过运行 `Set-IISCentralCertProviderCredential` 命令随时更改这个用户账户。

## 示例

### 示例 1
```
PS C:\> Set-IISCentralCertProviderCredential -UserName "IISCertificateAdmin"
```

此命令会将中央证书存储的用户账户更改为 IISCertificateAdmin。请注意，在调用 **Set-IISCentralCertProviderCredential** 时，只需指定用户名即可。命令运行后，系统会提示您输入该用户账户的密码。

## 参数

### -UserName
指定用于访问证书存储的用户账户；该账户可以是 Active Directory SAM 账户名称，也可以是用户主体名称。例如：

-UserName "IISCertificateAdmin"

建议您创建一个专门用于证书管理的用户账户，并仅授予该账户管理证书存储所需的权限（最重要的是，该账户需要具有对存储位置的读取访问权限）。中央存储的用户账户可以是本地账户，也可以是域账户。

请注意，您只需要指定用户账户名称即可。当命令实际运行时，系统会提示您输入用户账户密码。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### 无

## 输出

### 字符串

## 备注

## 相关链接

[Clear-IISCentralCertProvider](./Clear-IISCentralCertProvider.md)

[Disable-IISCentralCertProvider](./Disable-IISCentralCertProvider.md)

[Enable-IISCentralCertProvider](./Enable-IISCentralCertProvider.md)

[Get-IISCentralCertProvider](./Get-IISCentralCertProvider.md)

[Set-IISCentralCertProvider](./Set-IISCentralCertProvider.md)

