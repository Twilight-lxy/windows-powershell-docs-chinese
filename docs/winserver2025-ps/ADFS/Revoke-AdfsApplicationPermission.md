---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/revoke-adfsapplicationpermission?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Revoke-AdfsApplicationPermission
---

# 撤销 AdFS 应用程序权限

## 摘要
撤销对某个应用程序的访问权限。

## 语法

### 标识符（默认值）
```
Revoke-AdfsApplicationPermission [-TargetIdentifier] <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### RoleIdentifier
```
Revoke-AdfsApplicationPermission [[-TargetClientRoleIdentifier] <String>]
 [[-TargetServerRoleIdentifier] <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject
```
Revoke-AdfsApplicationPermission [-InputObject] <OAuthPermission> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Revoke-AdfsApplicationPermission` cmdlet 用于撤销 Active Directory Federation Services (AD FS) 中应用程序的权限。

## 示例

## 参数

### -InputObject
指定一个 **OAuthPermission** 对象。

```yaml
Type: OAuthPermission
Parameter Sets: InputObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetClientRoleIdentifier
```yaml
Type: String
Parameter Sets: RoleIdentifier
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -TargetIdentifier
```yaml
Type: String
Parameter Sets: Identifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetServerRoleIdentifier
```yaml
Type: String
Parameter Sets: RoleIdentifier
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行cmdlet之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于常用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft_identityServer.Management Resources.OAuthPermission

`OAuthPermission` 对象是通过 `InputObject` 参数接收到的。

### System.String

字符串对象通过 *TargetClientRoleIdentifier*、*TargetIdentifier* 和 *TargetServerRoleIdentifier* 参数被接收。

## 输出

## 备注

## 相关链接

[Get-AdfsApplicationPermission](./Get-AdfsApplicationPermission.md)

[Grant-AdfsApplicationPermission](./Grant-AdfsApplicationPermission.md)

[Set-AdfsApplicationPermission](./Set-AdfsApplicationPermission.md)

