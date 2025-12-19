---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IIS.Powershell.Commands.dll-Help.xml
Module Name: IISAdministration
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/iisadministration/set-iiscentralcertprovider?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-IISCentralCertProvider
---

# 设置 IISCentralCertProvider

## 摘要
为 IIS 中心证书存储设置属性值。

## 语法

```
Set-IISCentralCertProvider [-CertStoreLocation <String>] [-UserName <String>] [-Password <SecureString>]
 [-PrivateKeyPassword <SecureString>] [<CommonParameters>]
```

## 描述
`Set-IISCentralCertProvider` cmdlet 用于修改 IIS 中心证书存储的属性值。中心证书存储允许您将所有 IIS 证书集中存储在一个位置（例如文件存储中）；IIS 服务器随后会从这个集中位置检索证书信息。这意味着您只需在其中一个位置安装证书，无需在每台 IIS 服务器上都单独安装相同的证书。

`Set-IISCentralCertProvider` 通常在以下两种情况下使用：1) 当您需要更改证书存储的物理位置时（例如，如果您已将证书存储移动到了一个新的文件共享位置）；2) 当您运行了 `Clear-IISCentralCertProvider` cmdlet 并清除了所有证书存储属性值之后。在这些情况下，必须重新配置这些属性值，才能再次使用中央证书存储的功能。

## 示例

### 示例 1：修改中央证书存储的位置
```
PS C:\> Set-IISCentralCertProvider -CertStoreLocation "\\NewCertStoreServer\CertStore"
```

此命令用于修改 IIS 中央证书存储的位置。在这个示例中，证书存储已被移动到文件共享位置 `\\\\NewCertStoreServer\CertStore`。请注意，`Set-IISCentralCertProvider` 命令并不会将证书文件本身移动到新的位置；它只是配置证书存储以使用这个新的路径而已。

## 参数

### -CertStoreLocation
指定中央证书存储的物理路径；该路径可以是本地路径（例如：D:\CertStore），也可以是 UNC 路径。例如：

`-CertStoreLocation "\\\\CertStoreServer\CertStore"`

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
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

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -PrivateKeyPassword
用于指定您的 IIS 证书的私钥密码。例如：

`-PrivateKeyPassword "pa$$W0rd"`

只有当所有的 IIS 证书都使用相同的密码时，才应该使用这个参数。

```yaml
Type: SecureString
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -UserName
指定用于访问证书存储的用户账户；该账户可以是 Active Directory 的 SAM 账户名称，也可以是用户主体名称。例如：

`-UserName "IISCertificateAdmin"`

建议您创建一个专门用于证书管理的用户账户，并仅授予该账户管理证书存储所需的权限（最重要的是，该账户需要具有对存储位置的读取访问权限）。中央存储的用户账户可以是本地账户，也可以是域账户。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 about_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

### System.String

### System.Security.SecureString

## 输出

### System.Object

## 备注

## 相关链接

[Clear-IISCentralCertProvider](./Clear-IISCentralCertProvider.md)

[禁用IISCentralCertProvider](./Disable-IISCentralCertProvider.md)

[Enable-IISCentralCertProvider](./Enable-IISCentralCertProvider.md)

[Get-IISCentralCertProvider](./Get-IISCentralCertProvider.md)

[Set-IISCentralCertProviderCredential](./Set-IISCentralCertProviderCredential.md)

