---
description: 使用此主题来帮助您利用 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.HyperV.PowerShell.Cmdlets.dll-Help.xml
Module Name: Hyper-V
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hyper-v/new-vmgroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-VMGroup
---

# 新虚拟机组（New-VMGroup）

## 摘要
创建一个虚拟机组。

使用 Hyper-V 时，有两种类型的 VMGroup：VMCollectionType 和 ManagementCollectionType。VMCollectionType 类型的 VMGroup 包含虚拟机（VM），而 ManagementCollectionType 类型的 VMGroup 则包含其他 VMCollectionType 类型的 VMGroup。例如，你可以有两个 VMCollectionType 类型的 VMGroup，分别为 VMG1（包含虚拟机 VM1 和 VM2）和 VMG2（包含虚拟机 VM3 和 VM4）。然后你可以创建一个 ManagementCollectionType 类型的 VMGroup（名为 VM-All），该 VMGroup 包含这两个 VMCollectionType 类型的 VMGroup。你可以使用 [Add-VMGroupMember](./Add-VMGroupMember.md) cmdlet 将虚拟机添加到 VMCollectionType 类型的 VMGroup 中，或将多个 VMCollectionType 类型的 VMGroup 添加到 ManagementCollectionType 类型的 VMGroup 中。

## 语法

```powershell
New-VMGroup [-Name] <String> [-GroupType] <GroupType> [[-Id] <Guid>] [-CimSession <CimSession[]>]
 [-ComputerName <String[]>] [-Credential <PSCredential[]>] [<CommonParameters>]
```

## 描述
`New-VMGroup` cmdlet 用于创建一个虚拟机组。

## 示例

### 示例 1：创建一个用于包含虚拟机的组
```powershell
PS C:\> New-VMGroup -Name 'CollectionGroup07' -GroupType VMCollectionType
```

这个命令创建了一个名为 CollectionGroup07 的虚拟机组，其类型为 VMCollectionType。该组可以包含多个虚拟机集合（即由多个虚拟机组成的集合）。

### 示例 2：创建一个组来容纳多个虚拟机组
```powershell
PS C:\> New-VMGroup -Name 'ManagementCollectionGroup03' -GroupType ManagementCollectionType
```

此命令创建了一个名为ManagementCollectionGroup03的虚拟机组，其类型为ManagementCollectionType。该组可以包含其他组的集合。

## 参数

### -CimSession
在远程会话或远程计算机上运行该cmdlet。请输入计算机名称或会话对象（例如 `[New-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227967)` 或 `[Get-CimSession](https://go.microsoft.com/fwlink/p/?LinkId=227966)` cmdlet 的输出结果）。默认值为本地计算机上的当前会话。

```yaml
Type: CimSession[]
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -ComputerName
指定一个或多个运行此 cmdlet 的 Hyper-V 主机。允许使用 NetBIOS 名称、IP 地址和完全限定域名进行指定。默认值是本地计算机。可以使用 `localhost` 或点（.）来明确表示本地计算机。

```yaml
Type: String[]
Parameter Sets: (All)
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
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -GroupType
指定此cmdlet创建的组类型。该参数的可接受值为：ManagementCollectionType和VMCollectionType。

```yaml
Type: GroupType
Parameter Sets: (All)
Aliases:
Accepted values: VMCollectionType, ManagementCollectionType

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Id
指定此cmdlet创建的组的唯一ID。

```yaml
Type: Guid
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定此 cmdlet 创建的组的名称。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

### Microsoft.HyperV.PowerShell.VMGroup

## 备注

## 相关链接

[Get-VMGroup](./Get-VMGroup.md)

[Remove-VMGroup](./Remove-VMGroup.md)

[重命名虚拟机组](./Rename-VMGroup.md)

[Add-VMGroupMember](./Add-VMGroupMember.md)



