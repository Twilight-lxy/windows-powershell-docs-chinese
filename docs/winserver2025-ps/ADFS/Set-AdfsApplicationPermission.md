---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/set-adfsapplicationpermission?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AdfsApplicationPermission
---

# 设置 AdfsApplicationPermission

## 摘要
修改应用程序的权限。

## 语法

### 标识符（默认值）
```
Set-AdfsApplicationPermission [-TargetIdentifier] <String> [-ScopeNames <String[]>] [-Description <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### IdentifierAddScope
```
Set-AdfsApplicationPermission [-TargetIdentifier] <String> -AddScope <String[]> [-Description <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### IdentifierRemoveScope
```
Set-AdfsApplicationPermission [-TargetIdentifier] <String> -RemoveScope <String[]> [-Description <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject
```
Set-AdfsApplicationPermission [-InputObject] <OAuthPermission> [-ScopeNames <String[]>] [-Description <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObjectAddScope
```
Set-AdfsApplicationPermission [-InputObject] <OAuthPermission> -AddScope <String[]> [-Description <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObjectRemoveScope
```
Set-AdfsApplicationPermission [-InputObject] <OAuthPermission> -RemoveScope <String[]> [-Description <String>]
 [-WhatIf] [-Confirm] [<CommonParameters>]
```

### RoleIdentifier
```
Set-AdfsApplicationPermission [[-TargetClientRoleIdentifier] <String>] [[-TargetServerRoleIdentifier] <String>]
 [-ScopeNames <String[]>] [-Description <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### RoleIdentifierAddScope
```
Set-AdfsApplicationPermission [[-TargetClientRoleIdentifier] <String>] [[-TargetServerRoleIdentifier] <String>]
 -AddScope <String[]> [-Description <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### RoleIdentifierRemoveScope
```
Set-AdfsApplicationPermission [[-TargetClientRoleIdentifier] <String>] [[-TargetServerRoleIdentifier] <String>]
 -RemoveScope <String[]> [-Description <String>] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AdfsApplicationPermission` cmdlet 用于修改应用程序的权限设置。

## 示例

## 参数

### -AddScope
```yaml
Type: String[]
Parameter Sets: IdentifierAddScope, InputObjectAddScope, RoleIdentifierAddScope
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Description
指定一个描述。

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

### -InputObject
指定一个 **OAuthPermission** 对象。

```yaml
Type: OAuthPermission
Parameter Sets: InputObject, InputObjectAddScope, InputObjectRemoveScope
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -RemoveScope
```yaml
Type: String[]
Parameter Sets: IdentifierRemoveScope, InputObjectRemoveScope, RoleIdentifierRemoveScope
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ScopeNames
```yaml
Type: String[]
Parameter Sets: Identifier, InputObject, RoleIdentifier
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetClientRoleIdentifier
```yaml
Type: String
Parameter Sets: RoleIdentifier, RoleIdentifierAddScope, RoleIdentifierRemoveScope
Aliases:

Required: False
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetIdentifier
指定目标的标识符。

```yaml
Type: String
Parameter Sets: Identifier, IdentifierAddScope, IdentifierRemoveScope
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetServerRoleIdentifier
指定目标服务器角色的标识符。

```yaml
Type: String
Parameter Sets: RoleIdentifier, RoleIdentifierAddScope, RoleIdentifierRemoveScope
Aliases:

Required: False
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
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
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被执行。

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
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### System.String

`AddScope`、`Description`、`RemoveScope`、`ScopeNames`、`TargetClientRoleIdentifier`、`TargetIdentifier` 和 `TargetServerRoleIdentifier` 这些参数接收的是字符串对象。

### Microsoft.IdentityServer.Management.Resources.OAuthPermission

`OAuthPermission` 对象是通过 `InputObject` 参数接收到的。

## 输出

## 备注

## 相关链接

[Get-AdfsApplicationPermission](./Get-AdfsApplicationPermission.md)

[Grant-AdfsApplicationPermission](./Grant-AdfsApplicationPermission.md)

[Revoke-AdfsApplicationPermission](./Revoke-AdfsApplicationPermission.md)

