---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/enable-iiscentralcertprovider?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Enable-IISCentralCertProvider
---

# 启用 IISCentralCertProvider

## 摘要
启用 IIS 的中央证书存储功能。

## 语法

```
Enable-IISCentralCertProvider -CertStoreLocation <String> -UserName <String> -Password <SecureString>
 -PrivateKeyPassword <SecureString> [<CommonParameters>]
```

## 描述
**Enable-IISCentralCertProvider** cmdlet 可以启用 IIS 的中央证书存储功能。通过这个中央证书存储机制，你可以将所有的 IIS 证书集中存储在一个位置（例如文件共享文件夹）；IIS 服务器会从这个集中位置获取所需的证书。这样一来，你只需要在其中一个位置安装证书即可，无需在每台 IIS 服务器上都单独安装相同的证书。

当你安装中央证书存储时，默认情况下该存储是处于禁用状态的。要实际使用这一功能，你需要运行 **Enable-IISCentralCertProvider** cmdlet 命令。

## 示例

#### 示例 1：启用中央证书存储
```
PS C:\> Enable-IISCentralCertProvider -CertStoreLocation "\\CertStoreServer\CertStore" -UserName "IISCertificateAdmin" -Password "P@ssw0rd"
```

此命令启用了 IIS 的中央证书存储功能。在这个示例中，证书存储位于文件共享路径 “\\CertStoreServer\CertStore” 上，并且需要使用用户账户 “IISCertificateAdmin” 来访问该证书存储。

### 示例 2：启用中央证书存储并指定私钥密码
```
PS C:\> Enable-IISCentralCertProvider -CertStoreLocation "\\CertStoreServer\CertStore" -UserName "IISCertificateAdmin" -Password "P@ssw0rd" -PrivateKeyPassword "pa$$W0rd"
```

这个命令是示例1中所示命令的变体。然而，在示例2中，添加了*PrivateKeyPassword*参数，用于指定分配给所有IIS证书的私钥密码。

## 参数

### -CertStoreLocation
指定中央证书存储的物理路径；该路径可以是本地路径（例如：D:\CertStore），也可以是 UNC 路径。例如：

`-CertStoreLocation "\\\\CertStoreServer\CertStore"`

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Password
指定用于访问证书存储的用户账户的密码。例如：

`-密码 "P@ssw0rd"`

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PrivateKeyPassword
指定您的 IIS 证书的私钥密码。例如：

`-PrivateKeyPassword "pa$$W0rd"`

只有当所有的 IIS 证书都使用相同的密码时，才应该使用这个参数。

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -UserName
指定用于访问证书存储的用户账户；该账户可以是 Active Directory 的 SAM 账户名称，也可以是用户主体名称。例如：

`-UserName "IISCertificateAdmin"`

建议您创建一个专门用于证书管理的用户账户，并仅为该账户授予管理证书存储所需的权限（最重要的是，该账户需要具有对存储位置的读取访问权限）。证书存储的用户账户可以是本地账户，也可以是域账户。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters (http://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

### System.Security.SecureString

## 输出

### System.Object

## 备注

## 相关链接

[Clear-IISCentralCertProvider](./Clear-IISCentralCertProvider.md)

[Disable-IISCentralCertProvider](./ Disable-IISCentralCertProvider.md)

[Get-IISCentralCertProvider](./Get-IISCentralCertProvider.md)

[设置 IISCentralCertProvider](./Set-IISCentralCertProvider.md)

[设置 IISCentralCertProvider 凭据](./Set-IISCentralCertProviderCredential.md)

