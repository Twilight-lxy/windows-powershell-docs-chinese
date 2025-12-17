---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/get-adfsserverapplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Get-AdfsServerApplication
---

# 获取 AdfsServerApplication

## 摘要
获取在 AD FS 中某个应用程序的服务器应用角色的配置设置。

## 语法

### 标识符（默认值）
```
Get-AdfsServerApplication [[-Identifier] <String[]>] [<CommonParameters>]
```

### 名称
```
Get-AdfsServerApplication [-Name] <String[]> [<CommonParameters>]
```

### ApplicationObject
```
Get-AdfsServerApplication [-Application] <ServerApplication> [<CommonParameters>]
```

### ApplicationGroupIdentifier
```
Get-AdfsServerApplication [-ApplicationGroupIdentifier] <String> [<CommonParameters>]
```

### ApplicationGroupObject
```
Get-AdfsServerApplication [-ApplicationGroup] <ApplicationGroup> [<CommonParameters>]
```

## 描述
`Get-AdfsServerApplication` cmdlet 可以获取 Active Directory Federation Services (AD FS) 中某个应用程序的服务器应用角色的配置设置。

## 示例

## 参数

### -Application
指定要获取的服务器应用程序。

```yaml
Type: ServerApplication
Parameter Sets: ApplicationObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ApplicationGroup
指定用于获取服务器应用程序的应用程序组。

```yaml
Type: ApplicationGroup
Parameter Sets: ApplicationGroupObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -ApplicationGroupIdentifier
指定用于获取服务器应用程序的应用程序组的ID。

```yaml
Type: String
Parameter Sets: ApplicationGroupIdentifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Identifier
指定一个应用程序组ID数组，以便从中获取服务器应用程序。

```yaml
Type: String[]
Parameter Sets: Identifier
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Name
指定一个应用程序组名称的数组，以便从中获取服务器应用程序。

```yaml
Type: String[]
Parameter Sets: Name
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String[]
MicrosoftIdentityServer.Management.Resources.ServerApplication  
MicrosoftIdentityServer.Management.Resources.ApplicationGroup

## 输出

### Microsoft IdentityServer.Management.Resources.ServerApplication
ADUserPrincipalName                string  
ApplicationGroupIdentifier         string  
ClientSecret                  string  
Description                   string  
Enabled                         bool  
Identifier                      string  
JWKSUri                        uri  
JWTSigningCertificateRevocationCheck      Microsoft.IdentityServer.PolicyModel.Configuration.RevocationSetting  
JWTSigningKeys                   System.Collections.Generic.IDictionary<string, System.Object>  
Name                          string  
RedirectUri                     string[]

### Microsoft IdentityServer.PolicyModel.Configuration.RevocationSetting

RevocationSetting {  
    None = 0,  
    CheckEndCert = 1,  
    CheckEndCertCacheOnly = 2,  
    CheckChain = 3,  
    CheckChainCacheOnly = 4,  
    CheckChainExcludeRoot = 5,  
    CheckChain ExcludeRootCacheOnly = 6,  
}

## 备注
`Microsoft_identityServer.Management.Resources.ServerApplication` 继承自 `Microsoft IdentityServer.Management Resources.ClientApplication` 对象，并实现了 `MicrosoftIdentityServer.ManagementResources.IApplication` 接口。

MicrosoftIdentityServer.Management.Resources.ClientApplication

```
ApplicationGroupIdentifier                        string
Description                                       string
Enabled                                           bool
Identifier                                        string
Name                                              string
RedirectUri                                       string[]
```

Microsoft IdentityServer.ManagementResources.IApplication

ApplicationGroupIdentifier                          string  
Enabled                                              bool  
Name                                                  string

## 相关链接

[Add-AdfsServerApplication](./Add-AdfsServerApplication.md)

[Remove-AdfsServerApplication](./Remove-AdfsServerApplication.md)

[Set-AdfsServerApplication](./Set-AdfsServerApplication.md)
