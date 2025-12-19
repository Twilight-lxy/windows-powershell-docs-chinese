---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/remove-vmgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-VMGroup
---

# 删除虚拟机组（Remove-VMGroup）

## 摘要
删除一个虚拟机组。

## 语法

### 名称（默认值）
```
Remove-VMGroup [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Name] <String> [-Force] [<CommonParameters>]
```

### ID
```
Remove-VMGroup [-CimSession <CimSession[]>] [-ComputerName <String[]>] [-Credential <PSCredential[]>]
 [-Id] <Guid> [-Force] [<CommonParameters>]
```

### InputObject
```
Remove-VMGroup [-VMGroup] <VMGroup> [-Force] [<CommonParameters>]
```

## 描述
**Remove-VMGroup** cmdlet 用于删除一个虚拟机组。在删除某个虚拟机组之前，必须先确保该组中的所有虚拟机都已移除，即该组为空状态。

## 示例

### 示例 1：删除一个组
```
PS C:\> Remove-VMGroup -Name "Group04"
```

此命令会删除名为“Group04”的虚拟机组。在删除某个组之前，必须确保该组中的所有虚拟机都已关闭或移除，即该组必须是空的。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。可以输入计算机名称，或者输入一个会话对象（例如通过[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)或[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966) cmdlet获得的会话对象）。默认情况下，该cmdlet会在本地计算机的当前会话中执行。

```yaml
Type: CimSession[]
Parameter Sets: Name, Id
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个运行此cmdlet的Hyper-V主机。可以使用NetBIOS名称、IP地址或完全合格的域名进行指定。默认值为本地计算机。可以使用“localhost”或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: Name, Id
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Credential
指定一个或多个具有执行此操作权限的用户账户。默认值为当前用户。

```yaml
Type: PSCredential[]
Parameter Sets: Name, Id
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Force
强制命令运行，而无需询问用户确认。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Id
指定此 cmdlet 将要删除的空虚拟机组的唯一 ID。

```yaml
Type: Guid
Parameter Sets: Id
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定此 cmdlet 将要删除的空虚拟机组的名称。

```yaml
Type: String
Parameter Sets: Name
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VMGroup
指定一个空的虚拟机组，该虚拟机组将被此 cmdlet 删除。若要获取一个 **VMGroup** 对象，请使用 **Get-VMGroup** cmdlet。

```yaml
Type: VMGroup
Parameter Sets: InputObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### System.Object

## 备注

## 相关链接

[Get-VMGroup](./Get-VMGroup.md)

[New-VMGroup](./New-VMGroup.md)

[ Rename-VMGroup](./Rename-VMGroup.md)

