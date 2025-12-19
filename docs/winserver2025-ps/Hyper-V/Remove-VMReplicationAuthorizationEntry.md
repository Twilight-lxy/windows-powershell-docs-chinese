---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmreplicationauthorizationentry?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMReplicationAuthorizationEntry
---

# 删除 VM 复制授权条目

## 摘要
从副本服务器中删除授权条目。

## 语法

### PrimaryServerName（默认值）
```
Remove-VMReplicationAuthorizationEntry [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-AllowedPrimaryServer] <String> [-Passthru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

### TrustGroup
```
Remove-VMReplicationAuthorizationEntry [-CimSession <CimSession[]>] [-ComputerName <String[]>]
 [-Credential <PSCredential[]>] [-TrustGroup] <String> [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 对象
```
Remove-VMReplicationAuthorizationEntry [-VMReplicationAuthorizationEntry] <VMReplicationAuthorizationEntry[]>
 [-Passthru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-VMReplicationAuthorizationEntry` cmdlet 用于从副本服务器中删除授权条目，从而取消与该条目关联的主服务器的授权。删除授权条目后，副本服务器将不再接收来自相应主服务器的复制数据。

## 示例

### 示例 1
```
PS C:\> Remove-VMReplicationAuthorizationEntry -AllowedPrimaryServer server01.domain01.contoso.com
```

这个示例会从本地副本服务器中删除与允许的主服务器 server01.domain01.contoso.com 相关的授权记录。

### 示例 2
```
PS C:\> Get-VMReplicationAuthorizationEntry | Remove-VMReplicationAuthorizationEntry
```

这个示例会删除本地副本服务器上的所有授权记录。

## 参数

### -AllowedPrimaryServer
指定允许删除授权条目的主服务器。

```yaml
Type: String
Parameter Sets: PrimaryServerName
Aliases: AllowedPS

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中运行。

```yaml
Type: CimSession[]
Parameter Sets: PrimaryServerName, TrustGroup
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个需要从中删除授权条目的 Hyper-V 主机。可以使用 NetBIOS 名称、IP 地址或完全限定域名进行标识。默认值为本地计算机。可以使用 `localhost` 或点号（.`）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: PrimaryServerName, TrustGroup
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前，会提示您进行确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: PrimaryServerName, TrustGroup
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Passthru
指定需要将一个 **VMReplicationAuthorizationEntry** 对象传递给处理流程，该对象代表要被删除的授权条目。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
默认值 value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TrustGroup
指定要从中移除授权条目的信任组。

```yaml
Type: String
Parameter Sets: TrustGroup
Aliases:

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -VMReplicationAuthorizationEntry
指定要删除的授权条目。

```yaml
Type: VMReplicationAuthorizationEntry[]
Parameter Sets: Object
Aliases: VMRepAuthEntry

Required: True
Position: 0
默认值 value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。不过实际上并没有运行这个cmdlet。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
默认值 value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### 无
默认值

### VMReplicationAuthorizationEntry
如果指定了**-PassThru**选项……

## 备注

## 相关链接

